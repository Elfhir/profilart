from django.contrib import admin
from work.models import Work, WorkType

class WorkAdmin(admin.ModelAdmin):
    model = Work
    list_display = ('name', 'user', 'date_pub')
    list_filter = ['date_pub']
    search_fields = ['name']
    date_hierarchy = 'date_pub'
    
class WorkTypeAdmin(admin.ModelAdmin):
    model = WorkType
    list_display = ('idWork', 'idType')
    list_filter = ['idType']
    search_fields = ['idWork__name', 'idWork__user__username']
    
admin.site.register(Work, WorkAdmin)
admin.site.register(WorkType, WorkTypeAdmin)