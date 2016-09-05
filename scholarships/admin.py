from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Scholarship

admin.AdminSite.site_header = 'UndocuScholar Administration'

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'deadline', 'verified')
    list_filter = ['deadline', 'date_updated', 'verified']
    search_fields = ['name']
    fieldsets = [
        ('Scholarship Details', {
            'fields': ['name', 'deadline', 'amount', 'description', 'website', 'count']
        }),
        ('Scholarship Status',  {'fields': ['archived', 'verified']}),
    ]

admin.site.register(Scholarship, ScholarshipAdmin)