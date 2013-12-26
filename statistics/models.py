from django.db import models
from django.contrib.auth.models import User, ContentType

class FriendSocial(models.Model):
    user1 = models.ForeignKey(User, related_name="user1")
    user2 = models.ForeignKey(User, related_name="user2")
    date_pub = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s" % (self.id)