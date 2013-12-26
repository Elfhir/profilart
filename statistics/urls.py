from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^/$', 'statistics.views.display'),
    url(r'^/addfollow/$', 'statistics.views.addFollow'),
)