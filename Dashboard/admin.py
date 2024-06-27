from django.contrib import admin
from Dashboard.models import Site,Transaction_Category

# Register your models here.

@admin.register(Site)
class SiteModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Location','Contact','Status']

@admin.register(Transaction_Category)
class TCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['Date','Title','Type']