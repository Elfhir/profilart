from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from tastypie.api import Api
from exhibition.api import ExhibitionResource, CommentResource
from work.api import WorkResource
from authentification.api import UserResource

v1_api = Api(api_name='v1')
v1_api.register(ExhibitionResource())
v1_api.register(WorkResource())
v1_api.register(UserResource())
v1_api.register(CommentResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^search', include('searchengine.urls')),
    
    url(r'^ex/rateExhibition/(?P<session>\w+)/(?P<username>\w+)/(?P<IDExhibition>\w+)/(?P<rate>\w+)', 'exhibition.views.addExRate'),
    url(r'^ex/auth/(?P<username>\w+)/(?P<mdp>\w+)', 'authentification.views.authEx'),
    url(r'^ex/authsession/(?P<session>\w+)', 'authentification.views.authExSession'),
    url(r'^ex/commentexhibition/(?P<session>\w+)/(?P<username>\w+)/(?P<IDExhibition>\w+)/(?P<rate>\w+)/(?P<comment>[\w.!/?\,/_\-\ ]+)',
        'exhibition.views.addExComment'),
    
    url(r'^authentification', include('authentification.urls')),
    url(r'^(?P<username>\w+)', include('buildengine.urls')),
    url(r'^(?P<username>\w+)/work', include('work.urls')),
    url(r'^work/(?P<idWork>\w+)/$', 'work.views.home'),
    url(r'^(?P<username>\w+)/biography', 'buildengine.views.displayBio'),
    url(r'^(?P<username>\w+)/topic/(?P<nameTopic>.+)/$', 'work.views.displayTopic'),
    url(r'^(?P<username>\w+)/exhibitions/$', 'exhibition.views.displayFrontExhibition'),
    url(r'^(?P<username>\w+)/carteltopic/(?P<idTopic>.+)/$', 'work.views.displayCartelTopic'),
    url(r'^(?P<username>\w+)/cartel/(?P<idWork>.+)/$', 'work.views.displayCartelWork'),
    url(r'^(?P<username>\w+)/social', include('statistics.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^api/', include(v1_api.urls)),
)