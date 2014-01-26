# myapp/api.py
from tastypie.resources import ModelResource
from exhibition.models import Exhibition
from work.models import Work
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
        excludes = ['email', 'password', 'is_superuser', 'date_joined', 'is_staff', 'is_active', 'last_login', 'resource_uri']

class ExhibitionResource(ModelResource):   
    user = fields.ForeignKey(UserResource, 'user', full=True)
    class Meta:
        queryset = Exhibition.objects.all()
        resource_name = 'exhibition'
        filtering = {
            'date_pub': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'date_begin': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'date_end': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'mapLongitude': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'mapLatitude': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'zipcode': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }