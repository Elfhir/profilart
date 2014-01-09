from django import forms
from django.forms import ModelForm
from buildengine.models import *
from exhibition.models import *
from datetime import datetime
import json
import urllib2

class ExhibitionForm(forms.Form):
       nameGallery = forms.CharField()
       mapLongitude =  forms.FloatField(required=False, widget=forms.HiddenInput())
       mapLatitude =  forms.FloatField(required=False, widget=forms.HiddenInput())
       adress =  forms.CharField()
       zipcode = forms.IntegerField()
       country = forms.CharField()
       text = forms.CharField(widget=forms.Textarea)
       date_begin = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
       date_end = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker2'}))
       
       def save(self, request):
              URL = 'http://maps.googleapis.com/maps/api/geocode/json?address='+request.POST['adress']+'&sensor=false'
              response = urllib2.urlopen(URL)
              data = json.load(response)
              mapLatitude = data["results"][0]["geometry"]["location"]["lat"]
              mapLongitude = data["results"][0]["geometry"]["location"]["lng"]
              Exhibition(
                            nameGallery=request.POST['nameGallery'],
                            mapLongitude=mapLongitude,
                            mapLatitude=mapLatitude,
                            adress=request.POST['adress'],
                            content_type=ContentType.objects.get(model="exhibition"),
                            text=request.POST['text'],
                            zipcode=request.POST['zipcode'],
                            country=request.POST['country'],
                            date_begin=request.POST['date_begin'] ,
                            date_end=request.POST['date_end'],
                            user=request.user
                     ).save()