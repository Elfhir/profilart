from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('searchengine.views',
   url(r'^$', 'home'),
   url(r'^/compute-table-index$', 'computeAllTableIndex'),
   url(r'^/more-result$', 'getMoreResult'),
)