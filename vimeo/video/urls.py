""" URls file for video app """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.video_create_apiview),
]