from django.conf.urls import patterns, url
from frontpage import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^RobotPage/(?P<name>.*)', views.page),
    url(r'^Page/(?P<name>.*)', views.page),
  )
