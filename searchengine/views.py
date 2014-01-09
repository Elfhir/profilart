from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from work.models import *
from searchengine.models import *
from django.db.models.signals import *
from django.dispatch import receiver

@receiver(post_save, sender=Work)
def updateSaveAction(sender, **kwargs):
    print 'update save'
    workObject = kwargs['instance']
    WordsRate.objects.filter(work=workObject).delete()
    computeOneTableIndex(workObject)

def home(request):
    searchObject = request.POST
    searchWord = searchObject.get('the_search')
    return render(request, 'searchengine/home.html', locals())

def computeAllTableIndex(request):
    works = Work.objects.all()
    WordsRate.objects.all().delete()
    
    for work in works:
        computeOneTableIndex(work)
    
    wordsCount = WordsRate.objects.count()
            
    return render(request, 'searchengine/computeTableIndex.html', locals())


def computeOneTableIndex(work):
    print 'ComputeOneTableIndex'
    words = {}
    wordsParsed = []
    
    #caracteres a nettoyer
    charToRemove = [',', '.', '/', ':', ';', '?', '!', '(', ')', '"', "'"]
    
    words['titre'] = work.name.split()
    words['keywords'] = work.keywords.split()
    words['description'] = work.text.split()
    #nettoyage des mots et lowercase
    for key in words: 
        for i in range( len(words[key]) ):
            for c in charToRemove:
                words[key][i] = words[key][i].replace(c, '')
                words[key][i] = words[key][i].lower()
    
    for key in words:
        for word in words[key]:
            if( word not in wordsParsed ):
                wordRate = WordsRate(mot=word, rate=0, work=work)
                wordsParsed.append(word) 
            else:
                wordRate = WordsRate.objects.get(mot=word, work=work)
            
           
            wordRate.rate += Coeff.objects.get(name=key).coeff
            wordRate.save()
            print wordRate