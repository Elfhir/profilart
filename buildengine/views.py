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
        text = TextType.objects.get(user_id=user.id)
        prefWebsite = PrefWebsite.objects.get(user_id=user.id)
        images = ImageType.objects.filter(user_id=user.id).order_by("weight")
        workTopicType = WorkTopicType.objects.filter(idWork_id__user_id=user.id).order_by("idType").values_list("idType")
        lastWorks = Work.objects.filter(user_id=user.id).order_by("date_pub")[:3]
        firstname = user.first_name
        name = user.last_name
        editMode = False
        return render(request, 'buildengine/templates/template1/frontoffice/home.html', {'username' : username, 'blockText' : text, 'blockImage' : images,
                                                                       'lastWorks' : lastWorks, 'workType' : set(workTopicType), 'prefWebsite' : prefWebsite,
                                                                       'firstname' : firstname, 'name' : name, 'editMode' : editMode})
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
            text = TextType.objects.get(user_id=request.user.id)
            prefWebsite = PrefWebsite.objects.get(user_id=request.user.id)
            images = ImageType.objects.filter(user_id=request.user.id).order_by("weight")
            workType = WorkType.objects.all()
            works = Work.objects.all()
            firstname = user.first_name
            name = user.last_name
            pathTemplate = "buildengine/templates/template"+str(prefWebsite.id_template)+"/backoffice/home.html"
            editMode = True
            return render(request, 'buildengine/build.html', {'username' : username, 'blockText' : text, 'blockImage' : images,
                                                              'blockWork' : works, 'workType' : workType, 'prefWebsite' : prefWebsite,
                                                              'firstname' : firstname, 'name' : name, 'pathTemplate' : pathTemplate,
                                                              'editMode' : editMode})
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

def editText(request, username, idText):
    if userBackOfficePermission(request, username):
        defaultContent = TextType.objects.get(id=idText)
        textForm = TextForm(initial={'content': defaultContent})
        text = TextType.objects.get(user_id=request.user.id)
        #If the form has been sent
        if request.method == 'POST':
            form = TextForm(request.POST)
            if form.is_valid():
                requestContent = request.POST['content']
                text.text = requestContent
                text.save()
                text.full_clean()
                return HttpResponseRedirect("/"+username+"/build")
        return render(request, 'form/generator/text.html', {'form' : textForm, 'id' : idText})
    return HttpResponseRedirect("/") 

def addImage(request, username):
    if userBackOfficePermission(request, username):
        imageForm = ImageForm()
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                requestImage = request.FILES['file']            
                #Create new image in the database
                user = User.objects.get(username=username)
                path = USER_IMAGE_AVERAGE_PATH+requestImage.name
                contentType = ContentType.objects.get(model="imagetype")
                imageQuery = ImageType(user_id=user.id, path=path, content_type_id=contentType.id)
                imageQuery.save()
                imageQuery.full_clean()
                #half = 0.5
                #requestImageResized = requestImage.resize( [int(half * s) for s in im.size] )
                #default_storage.save(USER_IMAGE_AVERAGE_PATH+requestImage.name, ContentFile(requestImageResized.read()), quality=4)                
                return HttpResponseRedirect("/"+username+"/build")
        return render(request, 'form/generator/image.html', {'form' : imageForm})
    return HttpResponseRedirect("/") 

def deleteImage(request, username, idImage):
    if userBackOfficePermission(request, username):
        image = ImageType.objects.get(id=idImage)
        image.delete()
        return HttpResponseRedirect("/"+username+"/build")
    return HttpResponseRedirect("/") 

def userBackOfficePermission(request, username):
    sessionUserString = request.user.username.encode('utf8')
    usernameString = username.encode('utf8')
    if User.objects.filter(username=username).count():
        #If the user and the url are the same
        if sessionUserString == usernameString :
            return True
    return False   