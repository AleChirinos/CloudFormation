import json
import boto3
import os

users_table = os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

#Ejercicio 1
def getMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    user_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': 'movie_',
            'sk': 'title_'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("success")
    }

#Ejercicio 2 
def putMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(movie_id)
    item = {
        'pk': 'movie_id',
        'sk': 'title',
        'actors': body["actor"],
        'year': body["year"],
        'title': body["title"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('item')
    }
#Ejercicio 3
def getMovieDate(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(movie_id)
    response = table.get_item(
        Key={
            'pk': 'movie_',
            'sk': 'date_'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }



#Ejercicio 5
def getMovieByRoom(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    movie_id = path.split("/")[-3] # ["user", "id"]
    body = json.loads(event["body"])
    response = table.get_item(
        Key={
            'pk': 'room_id',
            'sk': 'movie_id'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }
    
#Ejercicio 6 
def getMovieByPerson(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    person_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(person_id)
    response = table.get_item(
        Key={
            'pk': 'person_',
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps('item')
    }

#Ejercicio 7 

def putPeople(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(room_id)
    item = {
        'pk': 'room_id',
        'sk': 'info',
        'room_people': body["room_people"],
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('item')
    }