# myapp/api.py
from tastypie.resources import ModelResource
from work.models import Work

class WorkResource(ModelResource):
    class Meta:
        queryset = Work.objects.all()
        resource_name = 'work'