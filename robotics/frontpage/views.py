from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from frontpage.models import * 

def index(request):
    header_picture = HeaderPicture.objects.all()[0]
    carousel_pictures = CarouselPicture.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'header_picture' : header_picture,
        'carousel_pictures' : carousel_pictures,
        })
    return HttpResponse(template.render(context))

def carousel(request):
    carousel_pictures = CarouselPicture.objects.all()
    template = loader.get_template('carousel.html')
    context = RequestContext(request, {
        'carousel_pictures' : carousel_pictures,
        })
    return HttpReponse(template.render(context))

# Create your views here.
