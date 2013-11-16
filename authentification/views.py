from django.shortcuts import render_to_response, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from authentification.form import LogInForm, RegisterForm

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
    return render_to_response('form/authentification.html', {'logInState' : 'Error identification', 'logInForm' : logInForm, 'registerForm' : registerForm})

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
            #If the user exists
            user = authenticate(username=requestUsername, password=requestPassword)
            if user is not None:
                if user.is_active:
                    #Starting the session of the user
                    login(request, user)
                    return HttpResponseRedirect("/")
    #At least one condition is false
    return render_to_response('form/authentification.html', {'registerState' : 'Error', 'logInForm' : logInForm, 'registerForm' : registerForm})
