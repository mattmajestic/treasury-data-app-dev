from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
import requests
import boto3
import torch
from transformers import pipeline

# AWS S3 configuration
s3 = boto3.client(
    's3',
    aws_access_key_id='<your_access_key_id>',
    aws_secret_access_key='<your_secret_access_key>'
)
bucket_name = '<your_bucket_name>'

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api_call_1")
async def api_call_1():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()

@app.get("/h20_ai")
async def h20_ai():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()

@app.get("/api_call_2")
async def api_call_2():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

@app.get("/api_call_3")
async def api_call_3():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_APP_ID")
    return response.json()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Treasury Insights API",
        version="0.1.0",
        description="Supplemental Treasury Insights Developer API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
