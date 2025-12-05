from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views.views import MovieViewSet, GenreViewSet, DirectorViewSet

router = DefaultRouter()

router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'directors', DirectorViewSet, basename='director')

urlpatterns = [
    path('', include(router.urls)),
]
