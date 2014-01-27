from django import template
from buildengine.models import PrefWebsite
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_username_from_userid(user_id):
    try:
        user = User.objects.get(id=user_id)
        anonymity = PrefWebsite.objects.get(user_id=user.id).anonymity
        if anonymity == 1:
            return user.username
        else:
            return user.first_name+" "+user.last_name
        
    except User.DoesNotExist:
        return 'Unknown'