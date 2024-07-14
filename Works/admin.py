from django.contrib import admin
from Works.models import ServiceCall

# Register your models here.

@admin.register(ServiceCall)
class ServiceCallModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Location','Number','Email','Description']