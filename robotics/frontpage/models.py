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

class Page(models.Model):
    title = models.CharField(max_length=200)
    images = models.ForeignKey(Picture, blank=True, null=True)

class PageGroup(models.Model):
    title = models.CharField(max_length=200)
    mainPage = models.ForeignKey(Page, blank=True, null=True)



# Create your models here.
