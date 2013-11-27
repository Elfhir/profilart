from work.form import *
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
                path = "/static/user_media/image/average/"+requestImage.name
                default_storage.save("static/user_media/image/average/"+requestImage.name, ContentFile(requestImage.read()))
                #Create Work in the database
                contentType = ContentType.objects.get(model="work")
                work = Work(name=requestName, text=requestText, user_id=user.id, imagepath=path, content_type_id=contentType.id)
                work.save()
                #Create WorkType in the database
                for value in requestType:
                    workType = WorkType(idType=value, idWork=work)
                    workType.save()
                return HttpResponseRedirect("/"+username+"/build")
        return render(request, 'form/addwork.html', {'form' : workForm})
    return HttpResponseRedirect("/")

def manageWork(request, username):
    if userBackOfficePermission(request, username):
        workType = WorkType.objects.all()
        works = Work.objects.all()
        return render(request, 'buildengine/managework.html', {'username' : username, 'blockWork' : works, 'workType' : workType})
    return HttpResponseRedirect("/")

def deleteWork(request, username, idWork):
    if userBackOfficePermission(request, username):
        work = Work.objects.filter(id=idWork)
        work.delete()
        return HttpResponseRedirect("/"+username+"/build")
    return HttpResponseRedirect("/")