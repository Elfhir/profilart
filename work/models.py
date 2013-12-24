from django.db import models
from django.contrib.auth.models import User, ContentType

class WorkTopic(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s" % (self.name)
    
class Work(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to="user_media/image/average/")
    content_type = models.ForeignKey(ContentType)
    work_topic = models.ForeignKey(WorkTopic)
    keywords = models.CharField(max_length=2000)
    date_created = models.DateTimeField(default='', null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    in_focus = models.BooleanField(default=False)
    material = models.CharField(max_length=2000)
    current_local = models.CharField(max_length=100)
    topview = models.BooleanField()
    weight = models.IntegerField(default=0)
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s" % (self.name)
    
class WorkTopicType(models.Model):
    idType = models.CharField(max_length=100)
    idWork = models.ForeignKey(WorkTopic)
    
    def __unicode__(self):
        return "%s" % (self.idType)
    
class WorkType(models.Model):
    idType = models.CharField(max_length=100)
    idWork = models.ForeignKey(Work)
    
    def __unicode__(self):
        return "%s" % (self.idType)