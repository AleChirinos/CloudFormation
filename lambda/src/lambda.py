import json
import boto3
import os

database = os.environ['MY_DATABASE']
language = os.environ['MAIN_LANGUAGE']

def handler(event, context):
    print(json.dumps({
        "database": database,
        "language": language
    }))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
