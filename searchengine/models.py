from django.db import models
from work.models import Work

class WordsRate(models.Model):
    mot = models.CharField(max_length=200) 
    rate = models.FloatField()
    work = models.ForeignKey(Work)
    
    def __unicode__(self):
        return "%s : %s" % (self.mot, self.rate)
    
class Coeff(models.Model):
    name = models.CharField(max_length=200) 
    coeff = models.FloatField()
    
    def __unicode__(self):
        return "%s : %s" % (self.name, self.coeff)
