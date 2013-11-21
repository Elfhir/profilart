from django.db import models
from django.contrib.auth.models import User, ContentType

class TextType(models.Model):
    text = models.CharField(max_length=3000)
    user = models.ForeignKey(User)
    weight = models.PositiveSmallIntegerField(default=0)
    content_type = models.ForeignKey(ContentType)
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s" % (self.text)
    
class ImageType(models.Model):
    user = models.ForeignKey(User)
    path = models.CharField(max_length=200)
    weight = models.PositiveSmallIntegerField(default=0)
    content_type = models.ForeignKey(ContentType)
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s" % (self.path)