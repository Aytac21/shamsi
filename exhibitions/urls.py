from django.urls import path
from . import views

app_name = 'exhibitions'

urlpatterns = [
    path('', views.exhibition_list, name='exhibition_list'),
    path('load-more-exhibitions/', views.load_more_exhibitions,
         name='load_more_exhibitions'),
    path('<int:pk>/', views.exhibition_detail, name='exhibition_detail'),
]
