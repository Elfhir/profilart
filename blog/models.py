from django.db import models
from django.contrib.auth.models import User

class Interview(models.Model):
    artiste = models.ForeignKey(User)
    auteur = models.CharField(max_length=100)
    contenu = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name="Date de parution")
    photo = models.ImageField(upload_to="blog/interview/")
    
    def __unicode__(self):
       return self.titre
    
class AnalyseCorpus(models.Model):
    contenu = models.TextField(null=False)
    auteur = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name="Date de parution")
    photo = models.ImageField(upload_to="blog/analyse-corpus/", blank=True)
    