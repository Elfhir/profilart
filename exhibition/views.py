from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from authentification.form import *
from buildengine.models import *
from exhibition.form import *
from work.models import *
from buildengine.views import userBackOfficePermission

def manageExhibitions(request, username):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        exhibitions = Exhibition.objects.filter(user_id=user.id)
        return render(request, 'buildengine/manageexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name,
                                                                     'exhibitions' : exhibitions})
    return HttpResponseRedirect("/")

def addExhibition(request, username):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        form = ExhibitionForm()
        if request.method == 'POST':
            form = ExhibitionForm(request.POST)
            if form.is_valid():
                form.save(request)
                return render(request, 'buildengine/manageexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name})
        return render(request, 'form/addexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name, 'form' : form})
    return HttpResponseRedirect("/")

def displayFrontExhibition(request, username):
    user = User.objects.get(username=username)
    exhibitions = Exhibition.objects.filter(user_id=user.id)
    prefWebsite = PrefWebsite.objects.get(user_id=user.id)
    firstname = user.first_name
    name = user.last_name
    workTopicType = WorkTopicType.objects.filter(idWork_id__user_id=user.id).order_by("idType").values_list("idType")
    return render(request, 'buildengine/templates/template'+str(prefWebsite.id_template)+'/frontoffice/exhibition.html', {'username' : username, 'exhibitions' : exhibitions,
                                                                    'prefWebsite' : prefWebsite, 'firstname' : firstname, 'name' : name,
                                                                    'workType' : set(workTopicType)})
