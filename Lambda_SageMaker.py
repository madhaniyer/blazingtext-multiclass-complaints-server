import os
import io
import boto3
import json
import csv


# grab environment variables 
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    data = json.loads(json.dumps(event))
    payload=data['sentences']
    
    #cloudwatch logging
    print('payload:', payload)
    # using the same nltk tokenizer that we used during data preparation for training
    payload = {"instances" : data['sentences']}

    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=json.dumps(payload))
                                       
    result = json.loads(response['Body'].read().decode())

    print(result)

    
    return result
