from django.contrib import admin
from .models import Team, Committee_list


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'session', 'image']

# admin.site.register(Team)
# admin.site.register(Committee_list)
@admin.register(Committee_list)
class Committee_listAdmin(admin.ModelAdmin):
    list_display = ['id', 'session']

