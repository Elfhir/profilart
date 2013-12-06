from django.contrib import admin
from buildengine.models import PrefWebsite

class PrefWebsiteAdmin(admin.ModelAdmin):
    model = PrefWebsite
    list_display = ('user', 'color', 'id_template')
    search_fields = ['user__username']

admin.site.register(PrefWebsite, PrefWebsiteAdmin)