from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
import requests
import boto3
from azure.storage.blob import BlockBlobService
from google.cloud import storage
import torch
from transformers import pipeline
import cirq

# AWS S3 configuration
#s3 = boto3.client(
    #'s3',
    #aws_access_key_id='<your_access_key_id>',
    #aws_secret_access_key='<your_secret_access_key>'
#)
#bucket_name = '<your_bucket_name>'

# Azure Setup
#account_name = '<your_storage_account_name>'
#account_key = '<your_storage_account_key>'
#block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
#container_name = '<your_container_name>'
#blob_name = '<your_blob_name>'
#file_path = '<path_to_your_local_file>'
# block_blob_service.create_blob_from_path(container_name, blob_name, file_path)

# GCP Setup
# Set up a client to interact with Google Cloud Storage
#client = storage.Client()

# Reference your bucket by name
#bucket_name = 'my-bucket-name'
# bucket = client.bucket(bucket_name)

# # Upload a file to the bucket
# blob = bucket.blob('example.txt')
# blob.upload_from_filename('/path/to/local/file.txt')

# # Download a file from the bucket
# blob = bucket.blob('example.txt')
# blob.download_to_filename('/path/to/local/destination.txt')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/quantum_ai")
async def quantum_ai():

    # Pick a qubit.
    qubit = cirq.GridQubit(0, 0)

    # Create a circuit
    circuit = cirq.Circuit(
        cirq.X(qubit)**0.5,  # Square root of NOT.
        cirq.measure(qubit, key='m')  # Measurement.
    )
    return circuit

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)
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
