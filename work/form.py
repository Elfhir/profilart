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

YES_OR_NO = [
    (True, 'Yes'),
    (False, 'No')
]

class WorkForm(forms.Form):
    name = forms.CharField(max_length=30)
    image = forms.FileField()
    text = forms.CharField(widget=forms.Textarea)
    keywords = forms.CharField(max_length=2000)
    dateCreated = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}), required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    depth = forms.IntegerField(required=False)
    in_focus = forms.BooleanField(widget=forms.RadioSelect(choices=YES_OR_NO), required=False)
    material = forms.CharField(max_length=2000, required=False)
    current_local = forms.CharField(max_length=100, required=False)
    type = forms.MultipleChoiceField(choices=TYPES, widget=forms.CheckboxSelectMultiple())
    
class WorkTopicForm(forms.Form):
    name = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)
    type = forms.MultipleChoiceField(choices=TYPES, widget=forms.CheckboxSelectMultiple())
    
class EditMetaWork(forms.Form):
    name = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)
    keywords = forms.CharField(max_length=2000)
    dateCreated = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}), required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    depth = forms.IntegerField(required=False)
    material = forms.CharField(max_length=2000, required=False)
    in_focus = forms.BooleanField(widget=forms.RadioSelect(choices=YES_OR_NO), initial=True, required=False)
    current_local = forms.CharField(max_length=100, required=False)
    type = forms.MultipleChoiceField(choices=TYPES, widget=forms.CheckboxSelectMultiple())
    
class EditImageWork(forms.Form):
    image = forms.FileField()