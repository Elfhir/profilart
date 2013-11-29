from django.db import models

class Interview(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    photo = models.ImageField(upload_to="blog/interview/")
    
    def __unicode__(self):
       return self.titre
   
   
class Corpus(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    
    
    def __unicode__(self):
       return self.titre
