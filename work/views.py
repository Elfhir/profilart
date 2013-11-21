from work.form import *
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from buildengine.models import *
from django.template import RequestContext
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from buildengine.form import TextForm, ImageForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def home(request, username, idWork):
    return HttpResponseRedirect("/")

def addWork(request, username):
    workForm = WorkForm()
    #If the form has been sent
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            requestName = request.POST['name']
            requestImage = request.FILES['image']  
            requestText = request.POST['text']
            requestType = request.POST.getlist('type')
            print requestType
            #Create new image in the database
            #user = User.objects.get(username=username)
            #path = "/static/user_media/image/average/"+requestImage.name
            #contentType = ContentType.objects.get(model="work")
            #imageQuery = ImageType(user_id=user.id, path=path, content_type_id=contentType.id)
            #imageQuery.save()
            #imageQuery.full_clean()
            #default_storage.save("static/user_media/image/average/"+requestImage.name, ContentFile(requestImage.read()))
            #Create Work in the database
            #work = Work(name=requestName, text=requestText, user_id=user.id, imagepath=path, content_type_id=contentType.id)
            #work.save()
            return HttpResponseRedirect("/"+username+"/build")
    return render(request, 'form/work.html', {'form' : workForm})