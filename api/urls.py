from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # path('films/', views.list_films),
    # path('films/<int:id>/', views.detail),
    # path('image/', views.create_film_image),
    # path('image/<int:id>/', views.delete_film_image),
    # path('film-attribute/', views.create_film_attr),
    # path('film-attribute/<int:id>/', views.update_delete_film_attr),
    path('films/', views.ListFilm.as_view()),
    path('films-create/', views.CreateFilm.as_view()),
    path('films-update/<int:id>/', views.UpdateFilm.as_view()),
    path('films/<int:id>/', views.DetailFilm.as_view()),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]