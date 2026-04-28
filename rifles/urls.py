from django.urls import path
from . import views

urlpatterns = [
    path("", views.rifle_list, name="rifle_list"),
    path("rifle/<int:id>/", views.rifle_detail, name="rifle_detail"),
    path("compare/", views.compare, name="compare"),
]