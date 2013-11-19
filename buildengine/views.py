from buildengine.models import *
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.models import User
from buildengine.form import TextForm

def home(request, username):
    #If the user exists
    if User.objects.filter(username=username).count():
        requestedUser = User.objects.get(username=username)
        text = [Text.objects.get(user_id=requestedUser.id), False]
        return render(request, 'buildengine/template/template1.html', {'username' : username, 'blockText' : text})
    return HttpResponseRedirect("/")

def backOffice(request, username):
    sessionUserString = request.user.username.encode('utf8')
    usernameString = username.encode('utf8')
    #If the user exists
    if User.objects.filter(username=username).count():
        #If the user and the url are the same
        if sessionUserString == usernameString :
            text = [Text.objects.get(user_id=request.user.id), True]
            return render(request, 'buildengine/build.html', {'username' : username, 'blockText' : text})
    return HttpResponseRedirect("/")

def editText(request, username, idText):
    #Default values of the form
    defaultContent = Text.objects.get(id=idText)
    textForm = TextForm(initial={'content': defaultContent})
    text = Text.objects.get(user_id=request.user.id)
    #If the form has been sent
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            requestContent = request.POST['content']
            text.text = requestContent
            text.save()
            return HttpResponseRedirect("/"+username+"/build")
    return render(request, 'form/generator/text.html', {'form' : textForm, 'id' : idText})
