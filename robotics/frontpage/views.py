from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from frontpage.models import Picture

def index(request):
    latest_pictures = Picture.objects
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_pictures' : latest_pictures,
        })
    return HttpResponse(template.render(context))

# Create your views here.
