from django import forms
from django.forms import ModelForm
from buildengine.models import *
from datetime import datetime

FONTS = [
       ('Arial', 'Arial'),
       ('Frutiger', 'Frutiger'),
    ]

class BioForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

class EditWebsiteForm(forms.Form):
    color = forms.CharField()
    font_color =  forms.CharField()
    font =  forms.ChoiceField(choices=FONTS, widget=forms.Select())   