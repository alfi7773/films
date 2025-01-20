from . import views
from django.urls import path

urlpatterns = [
    path('Films/', views.main, name='main'),
]