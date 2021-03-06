# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from work.models import *
from searchengine.models import *
from django.db.models.signals import *
from django.dispatch import receiver
from itertools import chain
import operator, random, copy

#caracteres a remplacer
charToRemplace = {  'a': [u'à', u'ã', u'á', u'â'],
                    'e': [u'é', u'è', u'ê', u'ë'],
                    'i': [u'î', u'ï'],
                    'u': [u'ù', u'ü', u'û'],
                    'o': [u'ô', u'ö'],
                    'c': [u'ç'],
                    '': [',', '.', '/', ':', ';', '?', '!', '(', ')', '"', "'"]
                    }

#mots à ignorer
wordToIgnore = ['les', 'elle', 'ils', 'elles', 'lui', 'moi', 'toi', 'nous', 'vous', 'soi', 'leur', 'eux',
                'celui', 'celle', 'ceux', 'ceci', 'cela', 'celles',
                'mien', 'tien', 'sien', 'mienne', 'tienne', 'sienne', 'miens', 'tiens', 'siens', 'miennes', 'tiennes', 'siennes', 'notre', 'votre', 'notres', 'votres', 'leurs',
                'qui', 'que', 'quoi', 'dont', 'ou', 'lequel', 'auxquel', 'duquel', 'laquelle', 'lesquels', 'auxquels', 'desquels', 'lesquelles', 'auxquelles', 'desquelles',
                'tout', 'une', 'uns', 'unes', 'aucun', 'aucune', 'aucuns' 'aucunes', 'tel', 'telle', 'tels', 'telles', 'toute',
                'suivant', 'apres', 'dela', 'hormis', 'par', 'sur', 'depuis', 'hors', 'parmi', 'avant', 'derriere', 'jusque', 'pendant', 'vers', 'avec', 'des', 'pour', 'chez', 'devant', 'pres', 'voici', 'voila', 'comme', 'malgre', 'moins', 'entre', 'sauf', 'contre','dans', 'sous', 'selon']


@receiver(post_save, sender=Work)
def updateSaveAction(sender, **kwargs):
    print 'update save'
    workObject = kwargs['instance']
    WordsRate.objects.filter(work=workObject).delete()
    computeOneTableIndex(workObject)


def home(request):
    searchObject = request.GET
    searchWord = searchObject.get('the_search')
    searchModalite = searchObject.get('modalite-recherche')
    # Recherche par défault
    if searchModalite is None:
        searchModalite = 'Simple'
    searchWordSplited = searchWord.lower().split()
    #On ne recherche que les mots d'une certaine taille et non ignorés
    searchWordSplited = [word for word in searchWordSplited if ( len(word) > 2 and word not in wordToIgnore )]
            
    #On remplace les signes indésirables (accents...)
    for i in range( len(searchWordSplited) ):
            for char, old_chars  in charToRemplace.items():
                for old_char in old_chars:
                    searchWordSplited[i] = searchWordSplited[i].replace(old_char, char)
    #print searchWordSplited
    
    resultWord = {}
    for i in range( len(searchWordSplited) ):
        resultWord[i] = list(WordsRate.objects.filter(mot=searchWordSplited[i]).order_by('-rate'))
    #print resultWord
    
    # On ne recupere que les oeuvres regroupant tous les mots cles
    work = []
    workTmp = []
    
    # la taille de resultWord correspond au nombre de mots recherchés dans la chaine nettoyée
    for i in range( len(resultWord) ):
        for j in range( len(resultWord[i]) ):
            workTmp.append(resultWord[i][j].work)
    #workTmp contient toutes les oeuvres contenant au moins un des mots recherché
    #print workTmp
    
    for i in range( len(workTmp)):
        # Si l'oeuvre recherchée i est contenu le même nombre de fois dans workTmp que le nombre de mots recherché alors celle-ci présente tous les mots clés
        # Donc si elle n'est pas deja ajouté à work on l'ajoute (2eme condition)
        if ( ( workTmp.count(workTmp[i]) == len(resultWord) ) and ( work.count(workTmp[i]) == 0 ) ):
            work.append(workTmp[i])
    #work ne contient que les oeuvres contant tous les mots-clé recherchés
    #print work
    
    if (searchModalite == 'Corpus'):
        nbCorpus = 3
        nbWorkByCorpus = 3
        corpuses = {}
        for i in range(nbCorpus):
            corpus = copy.deepcopy(work)
            random.shuffle(corpus)
            corpus = corpus[0:nbWorkByCorpus]
            print corpus
            corpuses[i] = corpus
        print corpuses
            
    
    
    return render(request, 'searchengine/home.html', locals())


def computeAllTableIndex(request):
    works = Work.objects.all()
    WordsRate.objects.all().delete()
    
    for work in works:
        computeOneTableIndex(work)
    
    wordsCount = WordsRate.objects.count()
            
    return render(request, 'searchengine/computeTableIndex.html', locals())


def getMoreResult(request):
    wordsRates = WordsRate.objects.order_by('mot')
    wordsNumb = {}
    for wr in wordsRates:
        if( wr.mot in wordsNumb):
            wordsNumb[wr.mot]+=1
        else:
            wordsNumb[wr.mot] = 1
    sorted_wordsNumb = sorted(wordsNumb.iteritems(), key=operator.itemgetter(1))
    sorted_wordsNumb.reverse()
    
    return render(request, 'searchengine/getMoreResult.html', locals())
    

def computeOneTableIndex(work):
    print 'ComputeOneTableIndex'
    words = {}
    wordsParsed = []

    words['titre'] = work.name.split()
    words['keywords'] = work.keywords.split()
    words['description'] = work.text.split()
    #nettoyage des mots et lowercase
    for key in words: 
        for i in range( len(words[key]) ):
            words[key][i] = words[key][i].lower()
            for char, old_chars  in charToRemplace.items():
                for old_char in old_chars:
                    words[key][i] = words[key][i].replace(old_char, char)
    
    for key in words:
        for word in words[key]:
            if( len(word) > 2 and word not in wordToIgnore):
                if( word not in wordsParsed ):
                    wordRate = WordsRate(mot=word, rate=0, work=work)
                    wordsParsed.append(word) 
                else:
                    wordRate = WordsRate.objects.get(mot=word, work=work)
                
               
                wordRate.rate += Coeff.objects.get(name=key).coeff
                wordRate.save()
                print wordRate
                
