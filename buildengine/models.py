from django.db import models
from django.contrib.auth.models import User, ContentType

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)

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
    
class PrefWebsite(models.Model):
    user = models.ForeignKey(User)
    id_template = models.PositiveIntegerField(default=1)
    color = models.CharField(max_length=10)
    font_family = models.CharField(max_length=50)
    
    def __unicode__(self):
        return "%s" % (self.user)