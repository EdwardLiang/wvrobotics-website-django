from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from frontpage.models import * 

def index(request):
    carousel_pictures = CarouselPicture.objects.all()
    if HeaderPicture.objects.all(): 
        header_picture = HeaderPicture.objects.all()[0]
    else:
        header_picture = None
    page_groups = PageGroup.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'carousel_pictures' : carousel_pictures,
        'header_picture' : header_picture,
        'page_groups' : page_groups,
        })
    return HttpResponse(template.render(context))

def navbar(request):
    header_picture = HeaderPicture.objects.all()
    template = loader.get_template('navbar.html')
    context = RequestContext(request, {
        'header_picture' : header_picture,
        })
    return HttpResponse(template.render(context))

def carousel(request):
    carousel_pictures = CarouselPicture.objects.all()
    template = loader.get_template('carousel.html')
    context = RequestContext(request, {
        'carousel_pictures' : carousel_pictures,
        })
    return HttpResponse(template.render(context))

def page(request, name="1"):
    if name == 1:
        return index(request)
    page = get_object_or_404(Page, title = name)
    template = loader.get_template('page.html')
    context = RequestContext(request, {
        'page': page, 'MEDIA_URL': settings.MEDIA_URL,
    })
    return HttpResponse(template.render(context))
    

# Create your views here.
