from django.urls import path
from . import views

app_name = 'workshop'

urlpatterns = [
    path('workshop/', views.gallery_view, name='workshop'),
    path('load-more-images/', views.load_more_images, name='load_more_images')
]
