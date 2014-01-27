from django import forms
from django.forms import ModelForm
from buildengine.models import *
from datetime import datetime

FONTS = [
       ('Arial', 'Arial'),
       ('Frutiger', 'Frutiger'),
    ]

MODE = [
       ('fade', 'fade'),
       ('horizontal', 'horizontal'),
       ('vertical', 'vertical'),
    ]

SPEED = [
       (6000, 'slow'),
       (3500, 'average'),
       (1500, 'fast'),
    ]

YES_OR_NO = [
    (True, 'Yes'),
    (False, 'No')
]

KIND_WORKS = [
    ('last', 'Last Works'),
    ('focus', 'Works in focus')
]
class BioForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

class EditWebsiteForm(forms.Form):
    color = forms.CharField()
    font_color =  forms.CharField()
    font =  forms.ChoiceField(choices=FONTS, widget=forms.Select())
    background = forms.FileField(required=False)
    
class SliderForm(forms.Form):
    mode = forms.ChoiceField(choices=MODE, widget=forms.Select())
    speed = forms.ChoiceField(choices=SPEED, widget=forms.Select())
    #auto = forms.BooleanField(widget=forms.RadioSelect(choices=YES_OR_NO), required=False)
    thumb = forms.BooleanField(widget=forms.RadioSelect(choices=YES_OR_NO), required=False)
    #ticker = forms.BooleanField(widget=forms.RadioSelect(choices=YES_OR_NO), required=False)
    kind_works = forms.ChoiceField(choices=KIND_WORKS, widget=forms.RadioSelect())
    
    def save(self, request):
        slider = PrefWebsiteSlider.objects.get(user_id=request.user.id)
        print request.POST
        slider.mode = request.POST['mode']
        slider.speed = request.POST['speed']
        slider.kind = request.POST['kind_works']
        if request.POST['thumb'] == "True":
            slider.thumb = True
        else:
            slider.thumb = False
        #if request.POST['auto'] == "True":
        #    slider.auto = True
        #else:
        #    slider.auto = False
        #if request.POST['ticker'] == "True":
        #    slider.ticker = True
        #else:
        #    slider.ticker = False
        slider.save()