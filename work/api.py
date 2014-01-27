# myapp/api.py
from tastypie.resources import ModelResource
from work.models import Work
from tastypie.serializers import Serializer
from datetime import datetime
from tastypie import fields
from django.utils import simplejson
from django.core.serializers import json
from django.contrib.auth.models import User
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_superuser', 'date_joined', 'is_staff', 'is_active', 'last_login', 'resource_uri']

class WorkResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    class Meta:
        limit = 3
        max_limit = 3
        queryset = Work.objects.filter(user_id__groups__name="Artist")
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post']
        resource_name = 'work'
        authorization = DjangoAuthorization()
        excludes = ["date_created"]
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'date_pub': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }