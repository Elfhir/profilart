from django import forms
from django.forms import ModelForm
from buildengine.models import *
from datetime import datetime

FONTS = [
       ('Arial', 'Arial'),
       ('Frutiger', 'Frutiger'),
    ]

class TextForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    
class ImageForm(forms.Form):
    file = forms.FileField()
    
class EditWebsiteForm(forms.Form):
    color = forms.CharField()
    font_color =  forms.CharField()
    font =  forms.ChoiceField(choices=FONTS, widget=forms.Select())   