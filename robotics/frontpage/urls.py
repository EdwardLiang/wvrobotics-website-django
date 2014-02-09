from django.conf.urls import patterns, url
from frontpage import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^carousel', views.carousel, name='carousel'),
    url(r'^navbar', views.navbar),
    url(r'^pages/(?P<name>.*)', views.page),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
