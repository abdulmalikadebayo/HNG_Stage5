# app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload_video_chunk', views.upload_video_chunk, name='upload_video_chunk'),
    path('play_video', views.render_video_page, name='play_video'),
    path('transcribe_video/', views.transcribe_video, name='transcribe_video'),
]
