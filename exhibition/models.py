from django.db import models
from django.contrib.auth.models import User, ContentType

class Exhibition(models.Model):
    nameGallery = models.CharField(max_length=100)
    mapLongitude =  models.FloatField (max_length=20)
    mapLatitude =  models.FloatField (max_length=20)
    adress =   models.CharField(max_length=100)
    city =   models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField()
    country =  models.CharField(max_length=20)
    user = models.ForeignKey(User)
    text = models.CharField(max_length=2000)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    rate = models.PositiveSmallIntegerField(null=True)
    content_type = models.ForeignKey(ContentType)
    date_update = models.DateTimeField(auto_now=True)
    date_pub = models.DateTimeField(auto_now=True)
    #artist = models.ManyToManyField(User, related_name="artist_user")
    
    def __unicode__(self):
       return self.nameGallery
    
class ExhibitionRate(models.Model):
    user = models.ForeignKey(User)
    rate = models.PositiveSmallIntegerField()
    exhibition = models.ForeignKey(Exhibition)
    date_pub = models.DateTimeField(auto_now=True)
        
    def __unicode__(self):
       return self.rate

class ExhibitionComment(models.Model):
    user = models.ForeignKey(User)
    exhibition = models.ForeignKey(Exhibition)
    content_type = models.ForeignKey(ContentType)
    text = models.CharField(max_length=2000)
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
       return self.user