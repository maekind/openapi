""" URls file for apiv1 """
from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:pk>/', views.video_detail_apiview),
    path('', include('video.urls')),
    # path('<int:pk>/best_quality/', views.xxx), => Return {id: {quality: url}}
    # path('<int:pk>/lowest_quality/', views.xxx), => Return {id: {quality: url}}
    # path('<int:pk>/qualities/', views.xxx), => Return {id: {quality1: url1, ..., qualityn: urln}}
    # path('<int:pk>/basic_info/', views.xxx), {id: {some basic propperties}}
    # path('<int:pk>/owner/', views.xxx), {id: {owner info}}
    # path('<int:pk>/bestquality/', views.xxx),

    # I can only retrieve information related to one video, because I don't clone Vimeo database.
    # My database grows with each api request.
]
