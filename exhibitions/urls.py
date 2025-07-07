from django.urls import path
from . import views

app_name = 'exhibitions'

urlpatterns = [    
    path('<int:pk>/', views.exhibition_detail, name='exhibition_detail'),
]
