from django import forms
from django.forms import ModelForm

GROUPS=[('1','Artist'),
        ('2','Curator'),
        ('3','Subscriber')]

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