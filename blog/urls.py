from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
   url(r'^$', 'home'),
   url(r'^archives/$', 'archives'),
   url(r'^archives/interview/(?P<id>\d+)$', 'interview'),
   url(r'^archives/analyse-corpus/(?P<id>\d+)$', 'analyseCorpus'),
   
   url(r'^admin/', include(admin.site.urls)),
)