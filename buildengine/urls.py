from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/$', 'buildengine.views.home'),
    url(r'^/build', 'buildengine.views.backOffice'),
)