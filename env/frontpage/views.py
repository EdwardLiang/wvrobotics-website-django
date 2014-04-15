from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from frontpage.models import * 

def index(request):
    template = loader.get_template('index.html')
    page = get_object_or_404(Page, title = 'index')
    context = RequestContext(request, {
        'page': page,
    })
    return HttpResponse(template.render(context))

def robotpage(request, name="1"):
    if name == 1:
        return index(request)
    page = get_object_or_404(Page, url_title = name)
    template = loader.get_template('robotpage.html')
    context = RequestContext(request, {
        'page': page,
    })
    return HttpResponse(template.render(context))

    
def page(request, name="1"):
    if name == 1:
        return index(request)
    page = Page.objects.get_subclass(url_title = name)
    if isinstance(type(page), RobotPage):
        return robotpage(request, name)
    elif isinstance(type(page), FrontPage):
        return index(request)
    else:
        template = loader.get_template('page.html')
    context = RequestContext(request, {
        'page': page,
    })
    return HttpResponse(template.render(context))
# Create your views here.
