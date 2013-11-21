from django import forms
from django.forms import ModelForm
from buildengine.models import *
from datetime import datetime

class TextForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    
class ImageForm(forms.Form):
    file = forms.FileField()
    