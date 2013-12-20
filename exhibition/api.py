# myapp/api.py
from tastypie.resources import ModelResource
from exhibition.models import Exhibition
from tastypie.serializers import Serializer
import time
from django.utils import simplejson
from django.core.serializers import json

class ExhibitionResource(ModelResource):
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