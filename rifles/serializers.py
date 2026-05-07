from rest_framework import serializers

from .models import (
    Manufacturer,
    Action,
    Caliber,
    Rifle,
    RifleVariant
)


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name']


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['id', 'name']


class CaliberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caliber
        fields = ['id', 'name']


class RifleVariantSerializer(serializers.ModelSerializer):
    caliber = CaliberSerializer(read_only=True)

    class Meta:
        model = RifleVariant

        fields = [
            'id',
            'sku',
            'name',
            'image_url',
            'caliber',
            'weight_lbs',
            'barrel_length_in',
            'twist_rate',
            'overall_length_in',
            'msrp'
        ]


class RifleSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)

    action = ActionSerializer(read_only=True)

    variants = RifleVariantSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Rifle

        fields = [
            'id',
            'manufacturer',
            'model',
            'action',
            'variants'
        ]