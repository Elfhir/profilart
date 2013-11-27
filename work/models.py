from django.db import models
from django.contrib.auth.models import User, ContentType

class Work(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    imagepath = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType)
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s" % (self.name)
    
class WorkType(models.Model):
    idType = models.PositiveSmallIntegerField()
    idWork = models.ForeignKey(Work)
    
    def __unicode__(self):
        return "%s" % (self.idType)