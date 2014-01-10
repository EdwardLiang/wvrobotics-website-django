from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to = 'images/')

class CarouselPicture(models.Model):
    image = models.ImageField(upload_to = 'image/carousel-front/')

class HeaderPicture(models.Model):
    image = models.ImageField(upload_to = 'image/')

class Caption(models.Model):
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text
# Create your models here.
