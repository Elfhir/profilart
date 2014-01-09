from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from authentification.form import *
from buildengine.models import *
from exhibition.form import *
from work.models import *
from buildengine.views import userBackOfficePermission
import json
import urllib2

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
        exhibitions = Exhibition.objects.filter(user_id=user.id)
        if request.method == 'POST':
            form = ExhibitionForm(request.POST)
            if form.is_valid():
                form.save(request)
                return render(request, 'buildengine/manageexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name,
                                                                             'exhibitions' : exhibitions})
        return render(request, 'form/addexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name, 'form' : form})
    return HttpResponseRedirect("/")

def editExhibition(request, username, idExhibition):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        exhibition = Exhibition.objects.get(id=idExhibition)
        exhibitions = Exhibition.objects.filter(user_id=user.id)
        form = ExhibitionForm(initial={'nameGallery':exhibition.nameGallery, 'mapLongitude':exhibition.mapLongitude, 'mapLatitude':exhibition.mapLatitude,
                                       'adress':exhibition.adress, 'zipcode':exhibition.zipcode, 'country':exhibition.country, 'text':exhibition.text,
                                       'date_begin':str(exhibition.date_begin)[0:10], 'date_end':str(exhibition.date_end)[0:10]})
        if request.method == 'POST':
            form = ExhibitionForm(request.POST)
            if form.is_valid():
                exhibition.mapLongitude = request.POST["mapLongitude"]
                exhibition.mapLatitude = request.POST["mapLatitude"]
                exhibition.adress = request.POST["adress"]
                print request.POST
                if request.POST["mapLongitude"] == "" or request.POST["mapLongitude"] == "0.0":
                    exhibition.mapLongitude = 0
                if request.POST["mapLatitude"] == "" or request.POST["mapLatitude"] == "0.0":
                    exhibition.mapLatitude = 0
                URL = 'http://maps.googleapis.com/maps/api/geocode/json?address='+exhibition.adress+'&sensor=false'
                response = urllib2.urlopen(URL)
                data = json.load(response)
                exhibition.mapLatitude = data["results"][0]["geometry"]["location"]["lat"]
                exhibition.mapLongitude = data["results"][0]["geometry"]["location"]["lng"]
                exhibition.nameGallery = request.POST["nameGallery"]
                exhibition.zipcode = request.POST["zipcode"]
                exhibition.country = request.POST["country"]
                exhibition.text = request.POST["text"]
                exhibition.date_begin = request.POST["date_begin"]
                exhibition.date_end = request.POST["date_end"]
                exhibition.save()
                #return render(request, 'buildengine/manageexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name,
                #'exhibitions' : exhibitions})
                return HttpResponseRedirect("/"+user.username+"/build/manageexhibitions/")
        return render(request, 'form/editexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name, 'form' : form, 'exhibition': exhibition})
    return HttpResponseRedirect("/")

def deleteExhibition(request, username, idExhibition):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        exhibitions = Exhibition.objects.filter(user_id=user.id)
        exhibition = Exhibition.objects.get(id=idExhibition)
        exhibition.delete()
        return render(request, 'buildengine/manageexhibition.html', {'firstname' : user.first_name, 'name' : user.last_name,
                                                                             'exhibitions' : exhibitions})
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
