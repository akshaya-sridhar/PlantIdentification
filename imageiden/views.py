from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from urllib.request import urlopen
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.urls import path
import os
import botocore
from django.core.files.storage import default_storage

import glob
import boto3
import json
import requests

# Create your views here.


def home(request):
    return render(request, 'index.html')


def diseasedetection(request):
    return render(request, 'diseasedetection.html')


def imagecapture(request):
    s3 = boto3.client('s3')
    if request.method == 'POST':
        image_path = request.POST["src"]
        image = NamedTemporaryFile()
        urlopen(image_path).read()
        image.write(urlopen(image_path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'  # store image in jpeg format
        image.name = name
        with open('image.txt', 'w+') as file:
            file.write(str(name))
        os.remove('C:\\Users\\aksha\\plant_iden\\plantpro\\media\\B.jpg')
        default_storage.save('C:\\Users\\aksha\\plant_iden\\plantpro\\media\\B.jpg', ContentFile(
            urlopen(image_path).read()))
        a = 'C:\\Users\\aksha\\plant_iden\\plantpro\\media\\B.jpg'
        # s3.Bucket('rekogniz1811').upload_file(a, '', ExtraArgs={'ACL':'public-read'})
        s3.upload_file(a, "rekogniz1812", "B.jpg",
                       ExtraArgs={'ACL': 'public-read'})

        # return HttpResponse('Done!')
        return redirect('aws/')

    return render(request, 'imagecapture.html')


@csrf_exempt
def save_image(request):
    if request.POST:
        # save it somewhere
        f = open(settings.MEDIA_ROOT + '/webcamimages/someimage.jpg', 'wb')
        f.write(request.raw_post_data)
        f.close()
        # return the URL
        return HttpResponse('http://localhost:8080/site_media/webcamimages/someimage.jpg')
    else:
        return HttpResponse('no data')


def awsdetect(request):
    b = ''
    try:
        s3 = boto3.resource('s3')
        model = 'arn:aws:rekognition:us-east-1:608940411829:project/PlantDetection/version/PlantDetection.2022-12-14T11.05.09/1670996110142'
        client = boto3.client('rekognition')
        # Call DetectCustomLabels
        response = client.detect_custom_labels(Image={'S3Object': {'Bucket': 'rekogniz1812', 'Name': 'B.jpg'}},
                                               MinConfidence=95,
                                               ProjectVersionArn=model)

        print(response['CustomLabels'])
        a = response['CustomLabels']
        for i in response['CustomLabels']:
            print('Label ' + str(i['Name']))
            b = i['Name']
            print('Confidence ' + str(i['Confidence']))
            print(b)
        app_id = 'da35d90f'
        app_key = '7fc86bc9688108fcd0ab1cce57884a7a'

        # url
        url = 'https://api.edamam.com/search?q=' + b + \
            '&app_id=' + app_id + '&app_key=' + app_key

        # get response
        response = requests.get(url)

        # get json
        data = response.json()

        # get recipes
        recipes = data['hits']

        # print recipes in json format
        print(json.dumps(recipes, indent=1))
                
    except:

        return HttpResponse('Nothing has been detected!!')

    return render(request, 'aws.html', {'b': b,'recipes':recipes})


def info(request):
    return render(request, 'description.html')
