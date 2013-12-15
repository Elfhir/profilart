from django import forms
from work.models import Work
from django.forms import ModelForm
import datetime

TYPES=[('1','Painting'),
       ('2','Photography'),
       ('3','Video'),
       ('4','Sculpture'),
       ('5','Installation'),
       ('6','Other')]

class WorkForm(forms.Form):
    name = forms.CharField(max_length=30)
    image = forms.FileField()
    text = forms.CharField(widget=forms.Textarea)
    keywords = forms.CharField(max_length=2000)
    dateCreated = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
    width = forms.IntegerField()
    height = forms.IntegerField()
    material = forms.CharField(max_length=2000)
    current_local = forms.CharField(max_length=100)
    type = forms.MultipleChoiceField(choices=TYPES, widget=forms.CheckboxSelectMultiple())
    
class WorkTopicForm(forms.Form):
    name = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)
    type = forms.MultipleChoiceField(choices=TYPES, widget=forms.CheckboxSelectMultiple())
    
class EditMetaWork(forms.Form):
    name = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)
    keywords = forms.CharField(max_length=2000)
    dateCreated = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
    width = forms.IntegerField()
    height = forms.IntegerField()
    material = forms.CharField(max_length=2000)
    current_local = forms.CharField(max_length=100)
    type = forms.MultipleChoiceField(choices=TYPES, widget=forms.CheckboxSelectMultiple())
    
class EditImageWork(forms.Form):
    image = forms.FileField()