
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('imagecapture',views.imagecapture, name='imagecapture'),
    path('aws/', views.awsdetect, name = 'aws'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)