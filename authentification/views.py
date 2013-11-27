from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from authentification.form import *
from buildengine.models import *
from buildengine.views import userBackOfficePermission
import os
                    
def authentification(request):
    logInForm = LogInForm();
    registerForm = RegisterForm();
    return render_to_response('form/authentification.html', {'logInForm' : logInForm, 'registerForm' : registerForm})

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
            textType = TextType.objects.create(text="Bonjour !", user_id = user.id, weight = 0, content_type_id = 10)
            prefWebsite = PrefWebsite.objects.create(user_id = user.id, id_template = 1, color = "#000", font_family="Arial")
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
        editAccountForm = EditAccountForm();
        if request.method == 'POST':
            form = EditAccountForm(request.POST)
            if form.is_valid():
                requestPassword = request.POST['password']
                requestConfirmPassword = request.POST['confirmPassword']
                requestEmail = request.POST['email']
                formState = "Error password"
                if requestPassword == requestConfirmPassword:
                    user = User.objects.get(username=username)
                    user.set_password(form.cleaned_data['password'])
                    user.email = requestEmail
                    user.save()
                    return HttpResponseRedirect("/"+username+"/build")
            return render(request, 'form/editaccount.html', {'form' : form, 'formState' : formState})
        return render(request, 'form/editaccount.html', {'form' : editAccountForm})
    return HttpResponseRedirect("/") 

def createUserFile(username):
    PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
    PATH_JOIN = os.path.join(PROJECT_PATH, 'user/' + username)
    if not os.path.exists(PATH_JOIN): os.makedirs(PATH_JOIN)
