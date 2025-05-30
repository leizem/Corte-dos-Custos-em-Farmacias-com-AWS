import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    volumes = ec2.describe_volumes(Filters=[{
        'Name': 'status',
        'Values': ['available']
    }])
    
    for volume in volumes['Volumes']:
        vol_id = volume['VolumeId']
        print(f"Excluindo volume {vol_id}")
        ec2.delete_volume(VolumeId=vol_id)
