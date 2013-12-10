from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from blog.models import Interview, AnalyseCorpus

def home(request):
    interview = Interview.objects.order_by('date')[0]
    return render(request, 'blog/home.html', locals())

def archives(request):
    interviews = Interview.objects.order_by('date')
    analyseCorpuses = AnalyseCorpus.objects.order_by('date')
    return render(request, 'blog/archives.html', locals())

def interview(request, id):
    interview = get_object_or_404(Interview, id=id)
    return render(request, 'blog/interview.html', locals())

def analyseCorpus(request, id):
    analyseCorpus = get_object_or_404(AnalyseCorpus, id=id)
    return render(request, 'blog/analyse-corpus.html', locals())