from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.list_films),
    path('films/<int:id>/', views.detail),
    path('image/', views.create_film_image),
    path('image/<int:id>/', views.delete_film_image),
    path('film-attribute/', views.create_film_attr),
    path('film-attribute/<int:id>/', views.update_delete_film_attr),
]