from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from authentification.form import *
from buildengine.models import *
from django.http import HttpResponse
from buildengine.views import userBackOfficePermission
import os
                    
def authentification(request):
    logInForm = LogInForm();
    registerForm = RegisterForm();
    return render_to_response('form/authentification.html', {'logInForm' : logInForm, 'registerForm' : registerForm})

def authEx(request, username, mdp):
    user = authenticate(username=username, password=mdp)
    #If the user exists
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse(str(request.session.session_key), content_type="text/plain")
    return HttpResponse("false", content_type="text/plain")

def authExSession(request, session):
    if(request.session.exists(session)):
        return HttpResponse("true", content_type="text/plain")
    else:
        return HttpResponse("false", content_type="text/plain")
    
def logOut(request):
    logout(request)
    return HttpResponseRedirect("/")

def loginUser(request):
    logInForm = LogInForm();
    registerForm = RegisterForm();
    #Retrieving the data from the request
    form = LogInForm(request.POST)
    if form.is_valid():
        requestUsername = request.POST['username']
        requestPassword = request.POST['password']
        #Creating a user
        user = authenticate(username=requestUsername, password=requestPassword)
        #If the user exists
        if user is not None:
            if user.is_active:
                #Starting the session of the user
                login(request, user)
                return HttpResponseRedirect("/")
    #At least one condition is false
    return render_to_response('form/authentification.html', {'logInForm' : form, 'registerForm' : registerForm})

def registerUser(request):
    logInForm = LogInForm();
    registerForm = RegisterForm();
    #Retrieving the data from the request
    form = RegisterForm(request.POST)
    if form.is_valid():
        requestUsername = request.POST['username']
        requestPassword = request.POST['password']
        requestConfirmPassword = request.POST['confirmPassword']
        requestFirstName = request.POST['firstName']
        requestLastName = request.POST['lastName']
        requestEmail = request.POST['email']
        requestGroup = request.POST['group']
        if requestPassword == requestConfirmPassword :
            #Creating new object User
            user = User.objects.create_user(requestUsername, requestEmail, requestPassword)
            user.is_active = 'true'
            user.first_name = requestFirstName
            user.last_name = requestLastName
            #Set group
            group = Group.objects.get(id=requestGroup)
            group.user_set.add(user)
            user.save()
            #Create file for this user
            #createUserFile(requestUsername)
            #Create pre-template
            prefWebsite = PrefWebsite.objects.create(user_id = user.id, id_template = 1, color = "#FFFFFF", font_color="#000000",
                                                     font_family="Arial")
            biography = Biography(user_id=user.id, text="").save()
            prefWebsiteSlider = PrefWebsiteSlider(user_id=user.id, mode="fade", speed=3500, thumb=False, auto=False, ticker=False, kind='last').save()
            #If the user exists
            user = authenticate(username=requestUsername, password=requestPassword)
            if user is not None:
                if user.is_active:
                    #Starting the session of the user
                    login(request, user)
                    return HttpResponseRedirect("/"+user.username+"/build")
    #At least one condition is false
    return render_to_response('form/authentification.html', {'logInForm' : logInForm, 'registerForm' : form})

def editAccount(request, username):
    if userBackOfficePermission(request, username):
        user = User.objects.get(username=username)
        prefWebsite = PrefWebsite.objects.get(user_id=user.id)
        editAccountForm = EditAccountForm();
        editAnonymityForm = EditAnonymityForm(initial={'anonymity' : prefWebsite.anonymity});
        if request.method == 'POST':
            form = EditAccountForm(request.POST)
            if form.is_valid():
                requestPassword = request.POST['password']
                requestConfirmPassword = request.POST['confirmPassword']
                requestEmail = request.POST['email']
                formState = "Error password"
                if requestPassword == requestConfirmPassword: 
                    user.set_password(form.cleaned_data['password'])
                    user.email = requestEmail
                    user.save()
                    return HttpResponseRedirect("/"+username+"/build")
            return render(request, 'form/editaccount.html', {'form' : form, 'form_anonymity' : editAnonymityForm, 'formState' : formState})
        return render(request, 'form/editaccount.html', {'form' : editAccountForm, 'form_anonymity' : editAnonymityForm})
    return HttpResponseRedirect("/")

def editAnonymity(request, username):
    if userBackOfficePermission(request, username):
        editAccountForm = EditAccountForm();
        editAnonymityForm = EditAnonymityForm();
        if request.method == 'POST':
            form = EditAnonymityForm(request.POST)
            if form.is_valid():
                    requestAnonymity = request.POST['anonymity']
                    user = User.objects.get(username=username)
                    prefWebsite = PrefWebsite.objects.get(user_id=user.id)
                    prefWebsite.anonymity = requestAnonymity
                    prefWebsite.save()
                    return HttpResponseRedirect("/"+username+"/build")
            return render(request, 'form/editaccount.html', {'form' : form, 'formState' : formState})
        return render(request, 'form/editaccount.html', {'form' : editAccountForm})
    return HttpResponseRedirect("/") 

def createUserFile(username):
    PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
    PATH_JOIN = os.path.join(PROJECT_PATH, 'user/' + username)
    if not os.path.exists(PATH_JOIN): os.makedirs(PATH_JOIN)
