from django.db import models
# from webcampicture.fields import WebcamPictureField

# class Child(models.Model):
#     name = models.CharField("Name", max_length=255)

#     # WebcamPictureField takes the same parameters as ImageField,
#     # besides the "width" and "height" positional parameters.
#     picture = WebcamPictureField(
#         "Picture", width=480, height=360, upload_to="media", blank=True
#     )

#     # Image URL example...
#     @property
#     def picture_url(self):
#         if self.picture and hasattr(self.picture, "url"):
#             return self.picture.url

# Create your models here.
# class Image(models.Model):
#     username = models.CharField(max_length=30)
#     image = models.ImageField(upload_to='images')
    
