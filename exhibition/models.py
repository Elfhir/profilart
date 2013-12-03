from django.db import models

class Exhibition(models.Model):
    
    
    def __unicode__(self):
       return self.titre