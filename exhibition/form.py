from django import forms
from django.forms import ModelForm
from buildengine.models import *
from datetime import datetime

class ExhibitionForm(forms.Form):
       nameGallery = forms.CharField()
       mapLongitude =  forms.FloatField()
       mapLatitude =  forms.FloatField()
       adress =  forms.CharField()
       zipcode = forms.IntegerField()
       text = forms.CharField(widget=forms.Textarea)
       date_begin = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
       date_end = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker2'}))
