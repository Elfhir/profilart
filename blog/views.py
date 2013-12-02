from django.shortcuts import render
from django.template import RequestContext
from blog.models import Interview, Corpus

def home(request):
    interview = Interview.objects.order_by('date')[0]
    return render(request, 'blog/home.html', locals())

def archives(request):
    interviews = Interview.objects.order_by('date')
    corpuses = Corpus.objects.order_by('date')
    return render(request, 'blog/archives.html', locals())