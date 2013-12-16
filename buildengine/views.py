from buildengine.models import *
from profilart.settings import USER_IMAGE_AVERAGE_PATH
from work.models import *
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from buildengine.form import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import Image

def home(request, username):
    #If the user exists
    if User.objects.filter(username=username).count():
        user = User.objects.get(username=username)
        prefWebsite = PrefWebsite.objects.get(user_id=user.id)
        workTopicType = WorkTopicType.objects.filter(idWork_id__user_id=user.id).order_by("idType").values_list("idType")
        lastWorks = Work.objects.filter(user_id=user.id).order_by("date_pub")[:3]
        firstname = user.first_name
        name = user.last_name
        return render(request, 'buildengine/templates/template1/frontoffice/home.html', {'username' : username, 'lastWorks' : lastWorks,
                                                                        'workType' : set(workTopicType), 'prefWebsite' : prefWebsite,
                                                                        'firstname' : firstname, 'name' : name,})
    return HttpResponseRedirect("/")

def backOffice(request, username):
    sessionUserString = request.user.username.encode('utf8')
    usernameString = username.encode('utf8')
    user = User.objects.filter(username=username)
    #If the user exists
    if user.count():
        #If the user and the url are the same
        if sessionUserString == usernameString :
            user = User.objects.get(username=username)
            prefWebsite = PrefWebsite.objects.get(user_id=request.user.id)
            workType = WorkType.objects.all()
            works = Work.objects.all()
            firstname = user.first_name
            name = user.last_name
            pathTemplate = "buildengine/templates/template"+str(prefWebsite.id_template)+"/backoffice/home.html"
            return render(request, 'buildengine/build.html', {'username' : username, 'blockWork' : works, 'workType' : workType,
                                                              'prefWebsite' : prefWebsite, 'firstname' : firstname, 'name' : name,
                                                              'pathTemplate' : pathTemplate,})
    return HttpResponseRedirect("/")

def editWebsite(request, username):
    prefWebsite = PrefWebsite.objects.get(user_id=request.user.id)
    colorDefault = prefWebsite.color
    fontColorDefault = prefWebsite.font_color
    fontStyleDefault = prefWebsite.font_family
    editWebsiteForm = EditWebsiteForm(initial={'color' : colorDefault, 'font' : fontStyleDefault, 'font_color' : fontColorDefault});
    if request.method == 'POST':
        form = EditWebsiteForm(request.POST)
        if form.is_valid():
            requestColor = request.POST['color']
            requestFont = request.POST['font']
            requestFontColor = request.POST['font_color']
            prefWebsite = PrefWebsite.objects.get(user_id=request.user.id)
            prefWebsite.color = requestColor
            prefWebsite.font_family = requestFont
            prefWebsite.font_color = requestFontColor
            prefWebsite.save()
            return HttpResponseRedirect("/"+username+"/build")
    return render(request, 'form/editwebsite.html', {'form': editWebsiteForm})

def editBio(request, username):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        bio = Biography.objects.get(user_id=user.id)
        bioForm = BioForm(initial={'text' : bio.text})
        prefWebsite = PrefWebsite.objects.get(user_id=user.id)
        pathTemplate = "buildengine/templates/template"+str(prefWebsite.id_template)+"/backoffice/bio.html"
        if request.method == 'POST':
            form = BioForm(request.POST)
            if form.is_valid():
                requestText = request.POST['text']
                bio.text = requestText
                bio.save()
                bioForm = BioForm(initial={'text' : bio.text})
        return render(request, 'buildengine/build.html', {'username' : username, 'prefWebsite' : prefWebsite, 'pathTemplate' : pathTemplate,
                                                        'firstname' : user.first_name, 'name' : user.last_name, 'form': bioForm})
    return HttpResponseRedirect("/") 

def displayBio(request, username):
    user = User.objects.get(username=username)
    prefWebsite = PrefWebsite.objects.get(user_id=user.id)
    bio = Biography.objects.get(user_id=user.id)
    firstname = user.first_name
    name = user.last_name
    return render(request, 'buildengine/templates/template1/frontoffice/bio.html', {'username' : username, 'prefWebsite' : prefWebsite,
                                                           'firstname' : firstname, 'name' : name, 'bio' : bio})

def userBackOfficePermission(request, username):
    sessionUserString = request.user.username.encode('utf8')
    usernameString = username.encode('utf8')
    if User.objects.filter(username=username).count():
        #If the user and the url are the same
        if sessionUserString == usernameString :
            return True
    return False