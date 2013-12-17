from django import forms
from django.forms import ModelForm
from buildengine.models import *
from datetime import datetime

class ExhibitionForm(forms.Form):
    nameGallery = forms.CharField(max_length=100)
    mapLongitude =  forms.FloatField (max_length=20)
    mapLatitude =  forms.FloatField (max_length=20)
    adress =  forms.CharField(max_length=100)
    zipcode = forms.PositiveIntegerField()
    text = forms.CharField(widget=forms.Textarea)
    date_begin = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
    date_end = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
