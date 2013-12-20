from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from authentification.form import *
from buildengine.models import *
from exhibition.form import *
from buildengine.views import userBackOfficePermission

def manageExhibitions(request, username):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        return render(request, 'buildengine/manageexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name})
    return HttpResponseRedirect("/")

def addExhibition(request, username):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        form = ExhibitionForm()
        return render(request, 'form/addexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name, 'form' : form})