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
       city =  forms.CharField()
       zipcode = forms.IntegerField()
       country = forms.CharField()
       text = forms.CharField(widget=forms.Textarea)
       date_begin = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
       date_end = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker2'}))
       
       def save(self, request):
			URLAddress = str(request.POST['adress']).replace(" ", "_")+"_"+str(request.POST['city']).replace(" ", "_")+"_"+str(request.POST['country']).replace(" ", "_")
			URL = 'http://maps.googleapis.com/maps/api/geocode/json?address='+URLAddress+'&sensor=false'
			response = urllib2.urlopen(URL)
			data = json.load(response)
			if data["results"][0] == "" :
				mapLatitude = -1
				mapLongitude = -1
			else :
				mapLatitude = data["results"][0]["geometry"]["location"]["lat"]
				mapLongitude = data["results"][0]["geometry"]["location"]["lng"]
			Exhibition(
						nameGallery=request.POST['nameGallery'],
						mapLongitude=mapLongitude,
						mapLatitude=mapLatitude,
						adress=request.POST['adress'],
						city = request.POST['city'],
						content_type=ContentType.objects.get(model="exhibition"),
						text=request.POST['text'],
						zipcode=request.POST['zipcode'],
						country=request.POST['country'],
						date_begin=request.POST['date_begin'] ,
						date_end=request.POST['date_end'],
						user=request.user
				 ).save()