from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('load-more-exhibitions/', views.load_more_exhibitions,
         name='load_more_exhibitions'),
]
