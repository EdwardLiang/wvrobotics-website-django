from django.db import models
from model_utils.managers import InheritanceManager


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
    carousel = models.ForeignKey(Carousel, blank=True, null=True)
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200)
    name_on_navbar = models.CharField(max_length=200)
    images = models.ManyToManyField(Picture, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    objects = InheritanceManager()
    class Meta:
        ordering = ['-priority',]
    def __unicode__(self):
        return self.title
    def classname(self):
        return self.__class__.objects.get_subclass(url_title = self.url_title).__class__.__name__
         
    
class FrontPage(Page):
    title = 'index'
    url_title = 'index'
    name_on_navbar = 'index'
    frontPageCarousel = models.ForeignKey(Carousel, blank=True, null=True)


class RobotPage(Page):
    robotName = models.CharField(max_length=200)
    challenge = models.CharField(max_length=200)
    leagueType = models.CharField(max_length=200)
    challengeDescription = models.TextField(blank=True, null=True)
    carousel2 = models.ForeignKey(Carousel, blank=True, null=True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-priority',]


class PageGroup(models.Model):
    title = models.CharField(max_length=200)
    pages = models.ManyToManyField(Page, blank=True, null=True)
    priority = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title


# Create your models here.
