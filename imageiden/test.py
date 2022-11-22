import boto3

client = boto3.client('rekognition')

modelarn = 'plantdataset.2022-11-21T18.51.55'

response = client.client.detect_custom_labels( ProjectVersionArn=modelarn, Image={'S3Object': {'Bucket': 'rekogniz1811','Name': 'B.jpg'} })
   
for data in response['CustomLabels']:
    print(data['Name'])
    print(data['Confidence'])