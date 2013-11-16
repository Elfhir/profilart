from django.conf.urls import patterns, include, url
from django.template import RequestContext

urlpatterns = patterns('',
   url(r'^$', 'blog.views.home'),
)