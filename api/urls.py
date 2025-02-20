from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .yasg import urlpatterns as url_doc


router = DefaultRouter()
router.register('films', views.FilmViewSet)
router.register('attributes', views.AttrApiModelViewSet)
router.register('images', views.ImageApiView)
router.register('categoriescategories', views.CategoryModelViewSet)
router.register('genres/', views.GenreModelViewsSet)


urlpatterns = [
    
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('auth/', include('api.auth.urls')),
    path('', include(router.urls))
]