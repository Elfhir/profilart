from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/$', 'buildengine.views.home'),
    url(r'^/build/$', 'buildengine.views.backOffice'),
    url(r'^/build/edit/text/(?P<idText>\w+)/$', 'buildengine.views.editText'),
)