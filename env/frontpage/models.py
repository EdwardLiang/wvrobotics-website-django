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
    def __unicode__(self):
        return self.name

class FrontPageCarousel(Carousel):
    def __unicode__(self):
        return self.name

class RobotCarousel(Carousel):
    def __unicode__(self):
        return self.name
   
class RobotBottomCarousel(Carousel):
    header_title = models.CharField(max_length=200)
    robot_pages = models.ManyToManyField('RobotPage', blank=True, null=True)
    def __unicode__(self):
        return self.name

class HeaderPicture(models.Model):
    image = models.ImageField(upload_to = 'images/') 

class Page(models.Model):
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
    frontPageCarousel = models.ForeignKey(FrontPageCarousel, blank=True, null=True)


class RobotPage(Page):
    challenge = models.CharField(max_length=200)
    leagueType = models.CharField(max_length=200)
    challengeDescription = models.TextField(blank=True, null=True)
    robot_carousel = models.ForeignKey(RobotCarousel, blank=True, null=True)
    robot_bottom_carousel = models.ForeignKey(RobotBottomCarousel, blank=True, null=True)
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
    class Meta:
        ordering = ['-priority',]


# Create your models here.
