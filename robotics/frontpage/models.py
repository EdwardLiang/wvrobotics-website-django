from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Background(models.Model):
    image = models.ImageField(upload_to = 'images/')

class Carousel(models.Model):
    images = models.ManyToManyField(Picture, blank=True, null=True)
    name = models.CharField(max_length=200)
    templateChoices = (
            ('leagueCarousel', 'league carousel'),
            ('frontpageCarousel', 'frontpage carousel'),
            ('robotCarousel', 'robot carousel'),
        )
    template = models.CharField(choices=templateChoices, default='ROBOTCAROUSEL', max_length=200)
    def __unicode__(self):
        return self.name

class HeaderPicture(models.Model):
    image = models.ImageField(upload_to = 'images/') 

class Page(models.Model):
    carousel = models.ManyToManyField(Carousel, blank=True, null=True)
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200)
    name_on_navbar = models.CharField(max_length=200)
    images = models.ManyToManyField(Picture, blank=True, null=True)
    text = models.CharField(max_length=2000, blank=True, null=True)
    def __unicode__(self):
        return self.title

class indexPage(Page):
    title = 'index'

class RobotPage(Page):
    robotName = models.CharField(max_length=200)
    challenge = models.CharField(max_length=200)
    leagueType = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title

class PageGroup(models.Model):
    title = models.CharField(max_length=200)
    pages = models.ManyToManyField(Page, blank=True, null=True)
    def __unicode__(self):
        return self.title



# Create your models here.
