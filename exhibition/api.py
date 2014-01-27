# myapp/api.py
from tastypie.resources import ModelResource
from exhibition.models import Exhibition
from work.models import Work
from buildengine.models import PrefWebsite
from django.contrib.auth.models import User
from tastypie.serializers import Serializer
import time
from tastypie import fields
from django.utils import simplejson
from django.core.serializers import json

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.filter(is_active=True)
        resource_name = 'user'
        excludes = ['email', 'password', 'is_superuser', 'date_joined', 'is_staff', 'is_active', 'last_login', 'resource_uri',
                    'first_name','last_name'
                    ]

class ExhibitionResource(ModelResource):   
    user = fields.ForeignKey(UserResource, 'user', full=True)
    
    class Meta:
        queryset = Exhibition.objects.filter()
        resource_name = 'exhibition'
        filtering = {
            'date_pub': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'date_begin': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'date_end': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'mapLongitude': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'mapLatitude': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'zipcode': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
    
    def dehydrate(self, bundle):
        bundle.data['work_preview'] = [str(x.image) for x in Work.objects.filter(user_id=bundle.obj.user.id)[:3]]
        bundle.data['anonymity'] = ''.join([str(x.anonymity) for x in PrefWebsite.objects.filter(user_id=bundle.obj.user.id)])
        if bundle.data['anonymity']:
            bundle.data['last_name'] = ''.join([str(x.last_name) for x in User.objects.filter(id=bundle.obj.user.id)])
            bundle.data['first_name'] = ''.join([str(x.first_name) for x in User.objects.filter(id=bundle.obj.user.id)])
        return bundle