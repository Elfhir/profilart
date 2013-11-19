from django import forms
from django.forms import ModelForm
from buildengine.models import Text

class TextForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)