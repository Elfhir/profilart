from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^/$', 'authentification.views.authentification'),
   url(r'^/login', 'authentification.views.loginUser'),
   url(r'^/register', 'authentification.views.registerUser'),
   url(r'^/logout', 'authentification.views.logOut'),
)