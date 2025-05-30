import json
import boto3
import base64
import gzip
from datetime import datetime
import re

def lambda_handler(event, context):
    """
    Função Lambda para processamento e análise de logs
    Trigger: CloudWatch Logs via subscription filter
    """
    
    cloudwatch = boto3.client('cloudwatch')
    
    try:
        # Decodificação dos dados de log
        cw_data = event['awslogs']['data']
        compressed_payload = base64.b64decode(cw_data)
        uncompressed_payload = gzip.decompress(compressed_payload)
        log_data = json.loads(uncompressed_payload)
        
        # Métricas para análise
        error_count = 0
        warning_count = 0
        total_requests = 0
        response_times = []
        
        # Processamento de cada evento de log
        for log_event in log_data['logEvents']:
            message = log_event['message']
            total_requests += 1
            
            # Detecção de erros
            if re.search(r'ERROR|Exception|Failed', message, re.IGNORECASE):
                error_count += 1
            
            # Detecção de warnings
            if re.search(r'WARN|Warning', message, re.IGNORECASE):
                warning_count += 1
            
            # Extração de tempo de resposta (assumindo formato específico)
            time_match = re.search(r'ResponseTime:(\d+)ms', message)
            if time_match:
                response_times.append(int(time_match.group(1)))
        
        # Cálculo de métricas
        avg_response_time = sum(response_times) / len(response_times) if response_times else 0
        error_rate = (error_count / total_requests) * 100 if total_requests > 0 else 0
        
        # Envio de métricas customizadas para CloudWatch
        metrics = [
            {
                'MetricName': 'ErrorCount',
                'Value': error_count,
                'Unit': 'Count'
            },
            {
                'MetricName': 'WarningCount', 
                'Value': warning_count,
                'Unit': 'Count'
            },
            {
                'MetricName': 'ErrorRate',
                'Value': error_rate,
                'Unit': 'Percent'
            },
            {
                'MetricName': 'AverageResponseTime',
                'Value': avg_response_time,
                'Unit': 'Milliseconds'
            }
        ]
        
        # Publicação das métricas
        for metric in metrics:
            cloudwatch.put_metric_data(
                Namespace='Abstergo/ApplicationLogs',
                MetricData=[{
                    'MetricName': metric['MetricName'],
                    'Value': metric['Value'],
                    'Unit': metric['Unit'],
                    'Timestamp': datetime.utcnow()
                }]
            )
        
        # Alertas para condições críticas
        if error_rate > 5:  # Mais de 5% de erro
            # Enviar alerta via SNS
            sns = boto3.client('sns')
            sns.publish(
                TopicArn=os.environ['ALERT_TOPIC_ARN'],
                Subject='Alerta: Alta Taxa de Erro Detectada',
                Message=f'Taxa de erro: {error_rate:.2f}% em {total_requests} requisições'
            )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'processed_events': len(log_data['logEvents']),
                'error_count': error_count,
                'warning_count': warning_count,
                'error_rate': error_rate,
                'avg_response_time': avg_response_time
            })
        }
        
    except Exception as e:
        print(f"Erro no processamento de logs: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {str(e)}')
        }