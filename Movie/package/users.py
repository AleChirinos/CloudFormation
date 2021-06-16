import json
import boto3
import os

users_table = os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)


def getMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    user_id = path.split("/")[-1] # ["user", "id"]
    # response = table.get_item(
    #     Key={
    #         'pk': user_id,
    #         'sk': 'age'
    #     }
    # )
    # item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("success")
    }

def putMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    user_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(user_id)
    # item = {
    #     'pk': user_id,
    #     'sk': 'age',
    #     'name': body["name"],
    #     'last_name': body["last_name"],
    #     'age': body["age"]
    # }
    # print(json.dumps(item))
    # table.put_item(
    #   Item=item
    # )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getMovieByRoom(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    user_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(user_id)
    # item = {
    #     'pk': user_id,
    #     'sk': 'age',
    #     'name': body["name"],
    #     'last_name': body["last_name"],
    #     'age': body["age"]
    # }
    # print(json.dumps(item))
    # table.put_item(
    #   Item=item
    # )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
