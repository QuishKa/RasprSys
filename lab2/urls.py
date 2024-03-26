from django.urls import path

from . import views

urlpatterns = [
    path("lab2/", views.index, name="lab2")
]