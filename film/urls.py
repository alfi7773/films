from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('film/<int:id>/', views.detail, name='detail'),
]