import json
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    """
    Função Lambda para envio de notificações multicanal
    Trigger: API Gateway ou SQS
    """
    
    # Inicialização de clientes AWS
    sns_client = boto3.client('sns')
    ses_client = boto3.client('ses')
    
    try:
        # Parse do payload
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event
        
        notification_type = body.get('type')
        recipient = body.get('recipient')
        message = body.get('message')
        subject = body.get('subject', 'Notificação Abstergo')
        
        # Validação de parâmetros obrigatórios
        if not all([notification_type, recipient, message]):
            return {
                'statusCode': 400,
                'body': json.dumps('Parâmetros obrigatórios ausentes')
            }
        
        results = []
        
        # Envio por email
        if notification_type in ['email', 'all']:
            try:
                email_response = ses_client.send_email(
                    Source=os.environ['FROM_EMAIL'],
                    Destination={'ToAddresses': [recipient]},
                    Message={
                        'Subject': {'Data': subject},
                        'Body': {
                            'Html': {'Data': f"<html><body>{message}</body></html>"},
                            'Text': {'Data': message}
                        }
                    }
                )
                results.append({
                    'channel': 'email',
                    'status': 'success',
                    'message_id': email_response['MessageId']
                })
            except Exception as e:
                results.append({
                    'channel': 'email',
                    'status': 'error',
                    'error': str(e)
                })
        
        # Envio por SMS
        if notification_type in ['sms', 'all']:
            try:
                sms_response = sns_client.publish(
                    PhoneNumber=recipient,
                    Message=message
                )
                results.append({
                    'channel': 'sms',
                    'status': 'success',
                    'message_id': sms_response['MessageId']
                })
            except Exception as e:
                results.append({
                    'channel': 'sms',
                    'status': 'error',
                    'error': str(e)
                })
        
        # Push notification
        if notification_type in ['push', 'all']:
            try:
                push_response = sns_client.publish(
                    TopicArn=os.environ['PUSH_TOPIC_ARN'],
                    Message=json.dumps({
                        'default': message,
                        'title': subject,
                        'body': message
                    }),
                    MessageStructure='json'
                )
                results.append({
                    'channel': 'push',
                    'status': 'success',
                    'message_id': push_response['MessageId']
                })
            except Exception as e:
                results.append({
                    'channel': 'push',
                    'status': 'error', 
                    'error': str(e)
                })
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Processamento de notificações concluído',
                'timestamp': datetime.utcnow().isoformat(),
                'results': results
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro interno: {str(e)}')
        }