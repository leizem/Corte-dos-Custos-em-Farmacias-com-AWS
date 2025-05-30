import json
import boto3
import os
from PIL import Image
import io

def lambda_handler(event, context):
    """
    Função Lambda para redimensionamento automático de imagens
    Trigger: S3 Event quando nova imagem é carregada
    """
    
    s3_client = boto3.client('s3')
    
    # Configurações
    MAX_WIDTH = 1920
    MAX_HEIGHT = 1080
    QUALITY = 85
    
    try:
        # Extração de informações do evento S3
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Validação de tipo de arquivo
        if not key.lower().endswith(('.jpg', '.jpeg', '.png')):
            return {
                'statusCode': 400,
                'body': json.dumps('Tipo de arquivo não suportado')
            }
        
        # Download da imagem original
        response = s3_client.get_object(Bucket=bucket, Key=key)
        image_data = response['Body'].read()
        
        # Processamento da imagem
        image = Image.open(io.BytesIO(image_data))
        
        # Redimensionamento mantendo proporção
        image.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)
        
        # Conversão para RGB se necessário
        if image.mode in ('RGBA', 'P'):
            image = image.convert('RGB')
        
        # Salvamento em buffer
        output_buffer = io.BytesIO()
        image.save(output_buffer, format='JPEG', quality=QUALITY, optimize=True)
        output_buffer.seek(0)
        
        # Upload da imagem processada
        processed_key = f"processed/{key}"
        s3_client.put_object(
            Bucket=bucket,
            Key=processed_key,
            Body=output_buffer.getvalue(),
            ContentType='image/jpeg',
            Metadata={
                'original-size': str(len(image_data)),
                'processed-size': str(len(output_buffer.getvalue())),
                'compression-ratio': str(round(len(output_buffer.getvalue()) / len(image_data), 2))
            }
        )
        
        # Log de sucesso
        print(f"Imagem processada: {key} -> {processed_key}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Imagem processada com sucesso',
                'original_key': key,
                'processed_key': processed_key,
                'original_size': len(image_data),
                'processed_size': len(output_buffer.getvalue())
            })
        }
        
    except Exception as e:
        print(f"Erro no processamento: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro interno: {str(e)}')
        }