from django.contrib import admin
from .models import Rifle

@admin.register(Rifle)
class RifleAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model", "caliber", "weight_lbs")
    search_fields = ("manufacturer", "model", "caliber")
    list_filter = ("manufacturer", "caliber")