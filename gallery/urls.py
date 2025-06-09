from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('gallery/', views.gallery_view, name='gallery'),
    path('videos/', views.gallery_video_view, name='gallery'),
    path('load-more-images/', views.load_more_images, name='load_more_images'),
    path('ajax/load-more-videos/', views.load_more_videos, name='load_more_videos'),
]
