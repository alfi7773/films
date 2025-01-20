from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.list_films),
    path('films/<int:id>/', views.detail),
]