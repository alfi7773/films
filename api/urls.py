from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('films/', views.ListCreateFilmApiView.as_view()),
    path('films/<int:id>/', views.UpdateDetailDeleteApiView.as_view()),
    path('image/', views.CreateImageApiView.as_view()),
    path('image/<int:id>/', views.DeleteImageApiView.as_view()),
    path('film-attribute/', views.CreateAttrApiView.as_view()),
    path('film-attribute/<int:id>/', views.UpdateDeleteAttrApiView.as_view()),
    # path('films/', views.ListFilm.as_view()),
    # path('films-create/', views.CreateFilm.as_view()),
    # path('films-update/<int:id>/', views.UpdateFilm.as_view()),
    # path('films/<int:id>/', views.DetailFilm.as_view()),
    # path('register/', views.RegisterView.as_view(), name='register'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]