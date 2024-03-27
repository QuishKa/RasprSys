from django.urls import path

from . import views

urlpatterns = [
    path("lab3/", views.index, name="lab3")
]