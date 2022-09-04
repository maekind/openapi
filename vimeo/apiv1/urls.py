""" URls file for apiv1 """
from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:pk>/', views.video_detail_apiview),
    path('', include('video.urls')),
]
