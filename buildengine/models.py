from django.db import models
from django.contrib.auth.models import User, ContentType

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)

class Biography(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=2000)
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s" % (self.text)
    
class PrefWebsite(models.Model):
    user = models.ForeignKey(User)
    id_template = models.PositiveIntegerField(default=1)
    anonymity = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=10)
    font_family = models.CharField(max_length=50)
    font_color = models.CharField(max_length=10)
    isvisible_homeslider = models.BooleanField()
    isvisible_homebio = models.BooleanField()
    isvisible_homeexhibition = models.BooleanField()
    color = models.CharField(max_length=10)
    
    def __unicode__(self):
        return "%s" % (self.user)
    
class PrefWebsiteSlider(models.Model):
    user = models.ForeignKey(User)
    mode = models.CharField(max_length=50)
    speed = models.PositiveIntegerField()
    thumb = models.BooleanField()
    auto = models.BooleanField()
    ticker = models.BooleanField()
    kind = models.CharField(max_length=10)
    
    def __unicode__(self):
        return "%s" % (self.mode)