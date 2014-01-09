from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to = 'images/')

class Caption(models.Model):
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text
# Create your models here.
