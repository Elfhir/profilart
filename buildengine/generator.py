from django.core.urlresolvers import reverse
from django.contrib.sites.models import get_current_site

def wrapperEdit(text, request):
    beginPath = request.build_absolute_uri(None)
    return "<div style='border: 1px dotted gray'>"+text.text+"</div><a href='"+beginPath+"/edit/"+text.content_type+"/"+str(text.id)+"'>Edit my element</a>"

def generateText(text, isEdit = False, request = None):
    if isEdit:
        content = "<div class='text'>"+text.text+"</div>"
        return wrapperEdit(text, request)
    else:
        return "<div class='text'>"+text.text+"</div>"
    
def get_absolute_url(self): 
    return reverse('project.app.views.view_name', None, [str(self.id)])