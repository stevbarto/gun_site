from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import (
    Rifle,
    RifleVariant,
    Caliber,
    Manufacturer
)

from .serializers import (
    RifleSerializer,
    RifleVariantSerializer,
    CaliberSerializer,
    ManufacturerSerializer
)


class RifleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rifle.objects.all()

    serializer_class = RifleSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]

    search_fields = [
        'manufacturer__name',
        'model'
    ]


class RifleVariantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RifleVariant.objects.all()

    serializer_class = RifleVariantSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]

    filterset_fields = [
        'caliber',
        'rifle',
    ]

    search_fields = [
        'name',
        'rifle__model'
    ]


class CaliberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Caliber.objects.all()

    serializer_class = CaliberSerializer


class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()

    serializer_class = ManufacturerSerializer