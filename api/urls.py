from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.list_films),
    path('film/<int:id>/', views.detail),
]