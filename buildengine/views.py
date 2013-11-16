from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.models import User

def home(request, username):
    #If the user exists
    if User.objects.filter(username=username).count():
        return render_to_response('buildengine/home.html', {'username' : username}, RequestContext(request))
    return HttpResponseRedirect("/")

def backOffice(request, username):
    sessionUserString = request.user.username.encode('utf8')
    usernameString = username.encode('utf8')
    #If the user exists
    if User.objects.filter(username=username).count():
        #If the user and the url are the same
        if sessionUserString == usernameString :
            return render_to_response('buildengine/build.html', {'username' : username}, RequestContext(request))
    return HttpResponseRedirect("/")