from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    text = models.CharField(max_length=3000)
    user = models.ForeignKey(User)
    content_type = models.CharField(max_length=10)
    
    def __unicode__(self):
        return "%s" % (self.text)