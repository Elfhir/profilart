from django.shortcuts import render_to_response, HttpResponseRedirect, render, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from authentification.form import *
from buildengine.models import *
from statistics.models import *
from buildengine.views import userBackOfficePermission
import os
                    
def addFollow(request, username):
    if request.is_ajax():
        if not request.user.is_authenticated():
            modal = 3
            return HttpResponse(modal)
        iduser = request.POST['iduser']
        requestiduser = request.POST['requestiduser']
        user1 = User.objects.get(id = requestiduser)
        user2 = User.objects.get(id = iduser)
        if user1 == user2:
            modal = 0
            return HttpResponse(modal)
        check = FriendSocial.objects.filter(user1_id = user1.id, user2_id = user2.id)
        if check:
            modal = 0
            return HttpResponse(modal)
        friendSocial = FriendSocial(user1 = user1, user2 = user2)
        friendSocial.save()
        modal = 1
    return HttpResponse(modal)
