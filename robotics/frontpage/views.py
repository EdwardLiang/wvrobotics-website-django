from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from frontpage.models import Picture

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        })
    return HttpResponse(template.render(context))

def carousel(request):
    latest_pictures = carousel_picture.objects
    template = loader.get_template('carousel.html')
    context = RequestContext(request, {
        'latest_pictures' : latest_pictures,
        })
    return HttpReponse(template.render(context))

# Create your views here.
