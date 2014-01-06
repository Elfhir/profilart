from django.db import models
from work.models import Work

class wordsRate(models.Model):
    mot = models.CharField(max_length=200) 
    rate = models.FloatField()
    work = models.ForeignKey(Work)
    
    def __unicode__(self):
        return "%s" % (self.mot + self.rate)
