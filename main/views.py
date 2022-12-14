from django.shortcuts import render
from django.http import JsonResponse
import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "tracker"
# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)
# Create your views here.

def home(request):
    return(render(request, "index.html"))


def getData(request):
    data = table.scan()
    print(data)
    return(JsonResponse({"data" : data['Items']}))