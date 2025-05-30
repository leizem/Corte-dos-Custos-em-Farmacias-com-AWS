#Interrompe instâncias EC2 com uso de CPU inferior a 5% por 24h.

import boto3
import datetime

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    ec2 = boto3.client('ec2')

    response = ec2.describe_instances(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=datetime.datetime.utcnow() - datetime.timedelta(days=1),
                EndTime=datetime.datetime.utcnow(),
                Period=86400,
                Statistics=['Average']
            )
            avg_cpu = metrics['Datapoints'][0]['Average'] if metrics['Datapoints'] else 100

            if avg_cpu < 5:
                print(f"Parando instância {instance_id} com CPU média de {avg_cpu}%")
                ec2.stop_instances(InstanceIds=[instance_id])
