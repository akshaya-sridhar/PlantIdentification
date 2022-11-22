from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from urllib.request import urlopen
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.urls import path
import os
from django.core.files.storage import default_storage


# Create your views here.

def home(request):
    return render(request, 'index.html')

def imagecapture(request):
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
        default_storage.save('C:\\Users\\aksha\\plant_iden\\plantpro\\media\\B.jpg', ContentFile(urlopen(image_path).read()))
        return HttpResponse('Done!')
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