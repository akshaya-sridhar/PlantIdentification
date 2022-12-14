
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('imagecapture',views.imagecapture, name='imagecapture'),
    path('diseasedetection',views.diseasedetection, name='diseasedetection'),
    path('aws/', views.awsdetect, name = 'aws'),
    path('info',views.info,name='info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)