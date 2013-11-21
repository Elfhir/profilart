from django import forms
from work.models import Work
from django.forms import ModelForm

TYPES=[('1','Paint'),
        ('2','Video'),
        ('3','Installation')]

class WorkForm(forms.Form):
    name = forms.CharField(max_length=30)
    image = forms.FileField()
    text = forms.CharField(widget=forms.Textarea)
    type = forms.MultipleChoiceField(choices=TYPES, widget=forms.CheckboxSelectMultiple())
    