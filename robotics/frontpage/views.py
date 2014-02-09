from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from frontpage.models import * 

def index(request):
    if HeaderPicture.objects.all(): 
        header_picture = HeaderPicture.objects.all()[0]
    else:
        header_picture = None
    if Background.objects.all():
        background = Background.objects.all()[0]
    else:
        background = None
    page = get_object_or_404(Page, title = 'index')
    page_groups = PageGroup.objects.all()
    carousels = page.carousel
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'carousels' : carousels, 
        })
    return HttpResponse(template.render(context))

def page(request, name="1"):
    if name == 1:
        return index(request)
    if HeaderPicture.objects.all(): 
        header_picture = HeaderPicture.objects.all()[0]
    else:
        header_picture = None
    page_groups = PageGroup.objects.all()
    page = get_object_or_404(Page, title = name)
    template = loader.get_template('page.html')
    context = RequestContext(request, {
        'page': page,
    })
    return HttpResponse(template.render(context))


# Create your views here.
