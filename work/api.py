# myapp/api.py
from tastypie.resources import ModelResource
from work.models import Work

class EntryResource(ModelResource):
    class Meta:
        queryset = Work.objects.all()
        resource_name = 'apiwork'