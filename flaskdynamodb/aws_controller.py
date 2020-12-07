import boto3

dynamo_client = boto3.client('dynamodb', region_name='us-west-2')

def get_items():
    return dynamo_client.scan(
        TableName='maricopa-sales-data'
    )