from django import forms
from django.forms import ModelForm
from buildengine.models import *
from exhibition.models import *
from datetime import datetime

class ExhibitionForm(forms.Form):
       nameGallery = forms.CharField()
       mapLongitude =  forms.FloatField()
       mapLatitude =  forms.FloatField()
       adress =  forms.CharField()
       zipcode = forms.IntegerField()
       country = forms.CharField()
       text = forms.CharField(widget=forms.Textarea)
       date_begin = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
       date_end = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker2'}))
       
       def save(self, request):
              Exhibition(
                            nameGallery=request.POST['nameGallery'],
                            mapLongitude=request.POST['mapLongitude'],
                            mapLatitude=request.POST['mapLatitude'],
                            adress=request.POST['adress'],
                            content_type=ContentType.objects.get(model="exhibition"),
                            text=request.POST['text'],
                            zipcode=request.POST['zipcode'],
                            country=request.POST['country'],
                            date_begin=request.POST['date_begin'] ,
                            date_end=request.POST['date_end'],
                            user=request.user
                     ).save()