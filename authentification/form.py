from django import forms
from django.forms import ModelForm

GROUPS=[('1','Artist'),
        ('2','Curator'),
        ('3','Subscriber')]

TYPE_OF_ANONYMITY=[('0','My name'),
                    ('1','My username')]

class LogInForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
        
class RegisterForm(forms.Form):
    firstName = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput())
    group = forms.ChoiceField(choices=GROUPS, widget=forms.RadioSelect())
    
class EditAccountForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    
class EditAnonymityForm(forms.Form):
    anonymity = forms.ChoiceField(choices=TYPE_OF_ANONYMITY, widget=forms.RadioSelect(), label = "I want to display :")