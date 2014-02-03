# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from exhibition.models import Exhibition, ExhibitionComment, ExhibitionRate
from work.models import Work
from buildengine.models import PrefWebsite
from django.contrib.auth.models import User
from tastypie.serializers import Serializer
import time
from tastypie import fields
from django.utils import simplejson
from django.core.serializers import json
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

        
class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.filter(is_active=True)
        resource_name = 'user'
        excludes = ['email', 'password', 'is_superuser', 'date_joined', 'is_staff', 'is_active', 'last_login', 'resource_uri',
                    'first_name', 'last_name']

class ExhibitionResource(ModelResource):   
    user = fields.ForeignKey(UserResource, 'user', full=True)
    class Meta:
        queryset = Exhibition.objects.filter(user_id__groups__name="Artist")
        resource_name = 'exhibition'
        excludes = ['rate']
        authorization = DjangoAuthorization()
        filtering = {
            'comment': ALL_WITH_RELATIONS,
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
        arrayRate = [x.rate for x in ExhibitionRate.objects.filter(exhibition = bundle.obj.id)]
        if(len(arrayRate) == 0):
            bundle.data['rateMedian'] = -1
        else:
            bundle.data['rateMedian'] = sum(arrayRate) / len(arrayRate)
        if not bundle.data['anonymity']:
            bundle.data['last_name'] = ''.join([str(x.last_name) for x in User.objects.filter(id=bundle.obj.user.id)])
            bundle.data['first_name'] = ''.join([str(x.first_name) for x in User.objects.filter(id=bundle.obj.user.id)])
        return bundle
    
class CommentResource(ModelResource):
    exhibition = fields.ForeignKey(ExhibitionResource, 'exhibition', full=True)
    class Meta:
        queryset = ExhibitionComment.objects.all()
        resource_name = 'comment'
        authorization = DjangoAuthorization()
        filtering = {
            'exhibition': ALL_WITH_RELATIONS
        }
        
    def dehydrate(self, bundle):
        bundle.data['username'] = bundle.obj.user.username
        bundle.data['rate'] = ''.join([str(x.rate) for x in ExhibitionRate.objects.filter(exhibition=bundle.obj.exhibition.id, user=bundle.obj.user.id)])
        return bundle

    
