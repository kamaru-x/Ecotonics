from django.contrib import admin
from Core.models import ServiceCategory,Service

# Register your models here.

@admin.register(ServiceCategory)
class ServiceCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','Date','Title']

@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id','Date','Category','Title']