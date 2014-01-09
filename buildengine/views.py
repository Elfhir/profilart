from buildengine.models import *
from buildengine.form import *
from profilart.settings import USER_IMAGE_AVERAGE_PATH
from work.models import *
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.models import User, Group
from exhibition.models import *
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import Image

def home(request, username):
    #If the user exists
    if User.objects.filter(username=username).count():
        user = User.objects.get(username=username)
        if user.groups.filter(name='Artist'):
            prefWebsite = PrefWebsite.objects.get(user_id=user.id)
            workTopicType = WorkTopicType.objects.filter(idWork_id__user_id=user.id).order_by("idType").values_list("idType")
            lastWorks = Work.objects.filter(user_id=user.id).order_by("date_pub")[:6]
            focusWorks = Work.objects.filter(user_id=user.id, in_focus=1).order_by("date_pub")[:6]
            firstname = user.first_name
            name = user.last_name
            biography = Biography.objects.get(user_id=user.id)
            lastExhibitions = Exhibition.objects.filter(user_id=user.id).order_by("date_pub")[:3]
            prefWebsiteSlider = PrefWebsiteSlider.objects.get(user_id=user.id)
            return render(request, 'buildengine/templates/template'+str(prefWebsite.id_template)+'/frontoffice/home.html', {'username' : username, 'lastWorks' : lastWorks,
                                                                            'workType' : set(workTopicType), 'prefWebsite' : prefWebsite,
                                                                            'firstname' : firstname, 'name' : name, 'biography': biography,
                                                                            'exhibitions': lastExhibitions, 'prefWebsiteSlider': prefWebsiteSlider, 'focusWorks': focusWorks, 'user': user})
        if user.groups.filter(name='Curator'):
            bio = Biography.objects.get(user_id=user.id)
            firstname = user.first_name
            name = user.last_name
            exhibitions = Exhibition.objects.filter(user=user.id)
            return render(request, 'buildengine/curator/home.html', {'firstname' : firstname, 'name' : name, 'biography' : bio,
                                                                     'exhibitions' : exhibitions})
    return HttpResponseRedirect("/")

def backOffice(request, username):
    sessionUserString = request.user.username.encode('utf8')
    usernameString = username.encode('utf8')
    #If the user exists
    user = User.objects.filter(username=username)
    if user.count():
        user = User.objects.get(username=username)
        if user.groups.filter(name='Artist'):
            #If the user and the url are the same
            if sessionUserString == usernameString :
                user = User.objects.get(username=username)
                prefWebsite = PrefWebsite.objects.get(user_id=request.user.id)
                workType = WorkType.objects.all()
                works = Work.objects.all()
                firstname = user.first_name
                name = user.last_name
                lastWorks = Work.objects.filter(user_id=user.id).order_by("date_pub")[:6]
                focusWorks = Work.objects.filter(in_focus=1, user_id=user.id).order_by("date_pub")[:6]
                biography = Biography.objects.get(user_id=user.id)
                lastExhibitions = Exhibition.objects.filter(user_id=user.id).order_by("date_pub")[:3]
                prefWebsiteSlider = PrefWebsiteSlider.objects.get(user_id=user.id)
                formSlider = SliderForm(initial={'mode': prefWebsiteSlider.mode, 'speed': prefWebsiteSlider.speed,
                                                 'thumb': prefWebsiteSlider.thumb, 'auto': prefWebsiteSlider.auto,
                                                 'ticker': prefWebsiteSlider.ticker, 'kind_works': prefWebsiteSlider.kind})
                pathTemplate = "buildengine/templates/template"+str(prefWebsite.id_template)+"/backoffice/home.html"
                return render(request, 'buildengine/build.html', {'username' : username, 'blockWork' : works, 'workType' : workType,
                                                                  'prefWebsite' : prefWebsite, 'firstname' : firstname, 'name' : name,
                                                                  'pathTemplate' : pathTemplate, 'lastWorks' : lastWorks,
                                                                  'biography': biography, 'exhibitions': lastExhibitions,
                                                                  'prefWebsiteSlider': prefWebsiteSlider, 'formSlider': formSlider, 'focusWorks': focusWorks})
        if user.groups.filter(name='Curator'):
            bio = Biography.objects.get(user_id=user.id)
            formBio = BioForm(initial={'text' : bio.text})
            firstname = user.first_name
            name = user.last_name
            exhibitions = Exhibition.objects.filter(user=user.id)
            return render(request, 'buildengine/curator/build.html', {'firstname' : firstname, 'name' : name, 'formBio' : formBio,
                                                                      'exhibitions' : exhibitions})
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
        if user.groups.filter(name='Artist'):
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
        if user.groups.filter(name='Curator'):
            if request.method == 'POST':
                form = BioForm(request.POST)
                if form.is_valid():
                    requestText = request.POST['text']
                    bio.text = requestText
                    bio.save()
                    bioForm = BioForm(initial={'text' : bio.text})
            return render(request, 'buildengine/curator/build.html', {'firstname' : user.first_name, 'name' : user.last_name, 'formBio' : bioForm})
    return HttpResponseRedirect("/")
    
def displayBio(request, username):
    user = User.objects.get(username=username)
    prefWebsite = PrefWebsite.objects.get(user_id=user.id)
    bio = Biography.objects.get(user_id=user.id)
    firstname = user.first_name
    name = user.last_name
    workTopicType = WorkTopicType.objects.filter(idWork_id__user_id=user.id).order_by("idType").values_list("idType")
    return render(request, 'buildengine/templates/template1/frontoffice/bio.html', {'username' : username, 'prefWebsite' : prefWebsite,
                                                           'firstname' : firstname, 'name' : name, 'bio' : bio, 'workType' : set(workTopicType)})

def switchVisible(request, username):
    if userBackOfficePermission(request, username):
        if request.is_ajax():
            user = User.objects.get(username=username)
            prefWebsite = PrefWebsite.objects.get(user_id=user.id)
            if request.POST['element'] == "homeslider":
                if request.POST['isVisible'] == "False":
                    prefWebsite.isvisible_homeslider = True
                else:
                    prefWebsite.isvisible_homeslider = False
            if request.POST['element'] == "homebio":
                if request.POST['isVisible'] == "False":
                    prefWebsite.isvisible_homebio = True
                else:
                    prefWebsite.isvisible_homebio = False
            if request.POST['element'] == "homeexhibition":
                if request.POST['isVisible'] == "False":
                    prefWebsite.isvisible_homeexhibition = True
                else:
                    prefWebsite.isvisible_homeexhibition = False
            prefWebsite.save()
    return HttpResponseRedirect("/")

def editSlider(request, username):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        form = SliderForm(request.POST)
        if form.is_valid():
            form.save(request)
        return HttpResponseRedirect("/"+user.username+"/build/")
    return HttpResponseRedirect("/")
    
def userBackOfficePermission(request, username):
    sessionUserString = request.user.username.encode('utf8')
    usernameString = username.encode('utf8')
    if User.objects.filter(username=username).count():
        #If the user and the url are the same
        if sessionUserString == usernameString :
            return True
    return False