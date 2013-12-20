from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from tastypie.api import Api
from exhibition.api import ExhibitionResource
from work.api import WorkResource

v1_api = Api(api_name='v1')
v1_api.register(ExhibitionResource())
v1_api.register(WorkResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^authentification', include('authentification.urls')),
    url(r'^(?P<username>\w+)', include('buildengine.urls')),
    url(r'^(?P<username>\w+)/work', include('work.urls')),
    url(r'^(?P<username>\w+)/biography', 'buildengine.views.displayBio'),
    url(r'^(?P<username>\w+)/topic/(?P<nameTopic>.+)/$', 'work.views.displayTopic'),
    url(r'^(?P<username>\w+)/carteltopic/(?P<idTopic>.+)/$', 'work.views.displayCartelTopic'),
    url(r'^(?P<username>\w+)/cartel/(?P<idWork>.+)/$', 'work.views.displayCartelWork'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^api/', include(v1_api.urls)),
)