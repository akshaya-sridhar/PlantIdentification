import boto3

# client = boto3.client('rekognition')

# modelarn = 'plantdataset.2022-11-21T18.51.55'

# response = client.client.detect_custom_labels( ProjectVersionArn=modelarn, Image={'S3Object': {'Bucket': 'rekogniz1811','Name': 'B.jpg'} })

# for data in response['CustomLabels']:
#     print(data['Name'])
#     print(data['Confidence'])

import os
import glob
import boto3

s3 = boto3.resource('s3')
model = 'arn:aws:rekognition:us-east-1:240133793648:project/plantdataset/version/plantdataset.2022-11-22T15.24.15/1669110856686'
client=boto3.client('rekognition')

#Call DetectCustomLabels
response = client.detect_custom_labels(Image={'S3Object': {'Bucket': 'rekogniz1811', 'Name': 'B.jpg'}},
    MinConfidence=1,
    ProjectVersionArn=model)

print(response)
# For object detection use case, uncomment below code to display image.
