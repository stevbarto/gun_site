from django.contrib import admin

from .models import (
    Manufacturer,
    Action,
    Caliber,
    Rifle,
    RifleVariant
)


class RifleVariantInline(admin.TabularInline):
    model = RifleVariant
    extra = 1


@admin.register(Rifle)
class RifleAdmin(admin.ModelAdmin):
    list_display = (
        'manufacturer',
        'model',
        'action'
    )

    search_fields = (
        'manufacturer__name',
        'model'
    )

    list_filter = (
        'manufacturer',
        'action'
    )

    inlines = [RifleVariantInline]


@admin.register(RifleVariant)
class RifleVariantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rifle',
        'caliber',
        'barrel_length_in',
        'weight_lbs',
        'msrp'
    )

    search_fields = (
        'name',
        'sku',
        'rifle__model'
    )

    list_filter = (
        'caliber',
        'rifle__manufacturer'
    )


@admin.register(Caliber)
class CaliberAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ('name',)