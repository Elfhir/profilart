from django.db import models
from django.contrib.auth.models import User, ContentType

class Exhibition(models.Model):
    nameGallery = models.CharField(max_length=100)
    mapLongitude =  models.FloatField (max_length=20)
    mapLatitude =  models.FloatField (max_length=20)
    adress =   models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField()
    curator = models.ForeignKey(User)
    text = models.CharField(max_length=2000)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    rate = models.PositiveSmallIntegerField()
    content_type = models.ForeignKey(ContentType)
    date_update = models.DateTimeField(auto_now=True)
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
       return self.nameGallery
    
class ExhibitionArtistCuratorLink(models.Model):
    #curator = models.ForeignKey(User, related_name='curator_targets')
    artist = models.ForeignKey(User, related_name='artist_targets')
    exhibition = models.ForeignKey(Exhibition)
    
    def __unicode__(self):
       return self.exhibition
    
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