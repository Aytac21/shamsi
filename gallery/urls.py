from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('gallery/', views.gallery_view, name='gallery'),
    path('load-more-images/', views.load_more_images, name='load_more_images'),
]
