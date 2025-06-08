from django.urls import path
from . import views

app_name = 'publications'

urlpatterns = [
    path('', views.publication_list, name='publication_list'),
    path('load-more/', views.load_more_publications,
         name='load_more_publications'),
    path('<int:pk>/', views.publication_detail, name='publication_detail'),
]
