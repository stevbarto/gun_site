from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rifles.views import (
    RifleViewSet,
    RifleVariantViewSet,
    CaliberViewSet,
    ManufacturerViewSet
)

router = DefaultRouter()

router.register(r'rifles', RifleViewSet)

router.register(
    r'variants',
    RifleVariantViewSet
)

router.register(
    r'calibers',
    CaliberViewSet
)

router.register(
    r'manufacturers',
    ManufacturerViewSet
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
]