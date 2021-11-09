from django.contrib import admin
from .models import Blood_donor

# Register your models here.

# Register your models here.
@admin.register(Blood_donor)
class Blood_donorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'district', 'blood_type','last_donate']
