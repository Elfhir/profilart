from work.form import *
from profilart.settings import USER_IMAGE_AVERAGE_PATH, BDD_USER_IMAGE_AVERAGE_PATH
from buildengine.views import userBackOfficePermission
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from buildengine.models import *
from work.models import *
from django.template import RequestContext
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from buildengine.form import TextForm, ImageForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
import StringIO
import os

def home(request, username, idWork):
    work = Work.objects.get(id=idWork)
    return render(request, 'buildengine/work.html', {'work' : work})

def addWork(request, username):
    if userBackOfficePermission(request, username):
        workForm = WorkForm()
        #If the form has been sent
        if request.method == 'POST':
            form = WorkForm(request.POST, request.FILES)
            if form.is_valid():
                requestName = request.POST['name']
                requestImage = request.FILES['image']  
                requestText = request.POST['text']
                requestType = request.POST.getlist('type')
                #Create new image in the database
                user = User.objects.get(username=username)
                #Create Work in the database
                contentType = ContentType.objects.get(model="work")
                work = Work(name=requestName, text=requestText, user_id=user.id, image=requestImage, content_type_id=contentType.id)
                work.save()
                #Create WorkType in the database
                for value in requestType:
                    workType = WorkType(idType=value, idWork=work)
                    workType.save()
                #Resize
                image = Image.open(work.image)
                image.thumbnail((820, 820), Image.ANTIALIAS)
                image.save(work.image.path)
                return HttpResponseRedirect("/"+username+"/build")
            return render(request, 'form/addwork.html', {'form' : form})
        return render(request, 'form/addwork.html', {'form' : workForm})
    return HttpResponseRedirect("/")

def manageWork(request, username):
    if userBackOfficePermission(request, username):
        workType = WorkType.objects.all()
        works = Work.objects.filter(user_id=request.user.id)
        return render(request, 'buildengine/managework.html', {'username' : username, 'blockWork' : works, 'workType' : workType})
    return HttpResponseRedirect("/")

def editWork(request, username, idWork):
    if userBackOfficePermission(request, username):
        work = Work.objects.get(id=idWork)
        editMetaWorkForm = EditMetaWork(initial={'name': work.name, 'text': work.text})
        editImageWorkForm = EditImageWork()
        #If the form has been sent
        if request.method == 'POST':
            form = EditMetaWork(request.POST, request.FILES)
            if form.is_valid():
                requestName = request.POST['name']
                requestText = request.POST['text']
                requestType = request.POST.getlist('type')
                work.name = requestName
                work.text = requestText
                work.save()
                WorkType.objects.filter(idWork_id=idWork).delete()
                for value in requestType:
                    workType = WorkType(idType=value, idWork=work)
                    workType.save()
                return HttpResponseRedirect("/"+username+"/build/editwork/"+idWork)
            return render(request, 'form/editwork.html', {'editMetaWorkForm' : form, 'editImageWorkForm' : editImageWorkForm,
                                                      'work': work})
        return render(request, 'form/editwork.html', {'editMetaWorkForm' : editMetaWorkForm, 'editImageWorkForm' : editImageWorkForm,
                                                      'work': work})
    return HttpResponseRedirect("/")

def editImageWork(request, username, idWork):
    if userBackOfficePermission(request, username):
        if request.method == 'POST':
            form = EditImageWork(request.POST, request.FILES)
            if form.is_valid():
                work = Work.objects.get(id=idWork)
                requestImage = request.FILES['image']
                work.image = requestImage
                work.save()
                #Resize
                image = Image.open(work.image)
                image.thumbnail((820, 820), Image.ANTIALIAS)
                image.save(work.image.path)
                return HttpResponseRedirect("/"+username+"/build/editwork/"+idWork)
        return HttpResponseRedirect("/"+username+"/build/editwork/"+idWork)
    return HttpResponseRedirect("/")

def deleteWork(request, username, idWork):
    if userBackOfficePermission(request, username):
        work = Work.objects.filter(id=idWork)
        work.delete()
        return HttpResponseRedirect("/"+username+"/build")
    return HttpResponseRedirect("/")