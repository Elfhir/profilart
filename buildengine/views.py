from buildengine.models import *
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from buildengine.form import TextForm, ImageForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def home(request, username):
    #If the user exists
    if User.objects.filter(username=username).count():
        requestedUser = User.objects.get(username=username)
        text = TextType.objects.get(user_id=requestedUser.id)
        images = ImageType.objects.filter(user_id=requestedUser.id).order_by("weight")
        editMode = False
        return render(request, 'buildengine/template/template1.html', {'username' : username, 'blockText' : text, 'blockImage' : images,
                                                                       'editMode' : editMode})
    return HttpResponseRedirect("/")

def backOffice(request, username):
    sessionUserString = request.user.username.encode('utf8')
    usernameString = username.encode('utf8')
    #If the user exists
    if User.objects.filter(username=username).count():
        #If the user and the url are the same
        if sessionUserString == usernameString :
            text = TextType.objects.get(user_id=request.user.id)
            images = ImageType.objects.filter(user_id=request.user.id).order_by("weight")
            editMode = True
            return render(request, 'buildengine/build.html', {'username' : username, 'blockText' : text, 'blockImage' : images,
                                                              'editMode' : editMode})
    return HttpResponseRedirect("/")

def editText(request, username, idText):
    #Default values of the form
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

def addImage(request, username):
    imageForm = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            requestImage = request.FILES['file']            
            #Create new image in the database
            user = User.objects.get(username=username)
            path = "/static/user_media/image/average/"+requestImage.name
            contentType = ContentType.objects.get(model="imagetype")
            imageQuery = ImageType(user_id=user.id, path=path, content_type_id=contentType.id)
            imageQuery.save()
            imageQuery.full_clean()
            default_storage.save("static/user_media/image/average/"+requestImage.name, ContentFile(requestImage.read()))          
            return HttpResponseRedirect("/"+username+"/build")
    return render(request, 'form/generator/image.html', {'form' : imageForm})

def deleteImage(request, username, idImage):
    image = ImageType.objects.get(id=idImage)
    image.delete()
    return HttpResponseRedirect("/"+username+"/build")