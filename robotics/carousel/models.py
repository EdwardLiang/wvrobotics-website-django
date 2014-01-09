from django.db import models

class Carousel(models.Model):
    image = models.ImageField(upload_to = 'assets/images/')
    def __unicode__(self):
        return self.image

class Picture(models.Model):
    image = models.ImageField(upload_to = 'assets/images/')
    def __unicode__(self):
        return self.image

class Caption(models.Model):
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text
# Create your models here.
