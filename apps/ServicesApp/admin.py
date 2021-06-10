from django.contrib import admin
from apps.ServicesApp import models

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields =('createDateService', 'updateDateService')
    list_display = ['titleService', 'contentService', 'imageService', 'createDateService', 'updateDateService']

admin.site.register(models.Service, ServiceAdmin)