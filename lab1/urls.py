from django.urls import path

from . import views

urlpatterns = [
    path("lab1/", views.index, name="lab1")
]