from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/(?P<idWork>\w+)/$', 'work.views.home'),
)