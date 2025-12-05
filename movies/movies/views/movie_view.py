from rest_framework import viewsets, status
from rest_framework.response import Response
from movies.serializers.serializers import MovieSerializer, MovieCreateUpdateSerializer
from movies.services.services import list_movies
from movies.models.models import Movie
from drf_spectacular.utils import extend_schema
from common.cache import cache_model_instance, get_cached_model, delete_cached_model

class MovieViewSet(viewsets.ViewSet):
    @extend_schema(
        request=None,
        responses={200: MovieSerializer(many=True)},
        summary="List movies",
        description="Returns list of movies"
    )
    def list(self, request) -> Response:
        filters = {
            "title": request.query_params.get("title"),
            "release_year": request.query_params.get("release_year")
        }
        queryset = list_movies(filters)
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        request=MovieCreateUpdateSerializer,
        responses={201: MovieSerializer},
        summary="Creating movie"
    )
    def create(self, request) -> Response:
        serializer = MovieCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.save()

        cache_model_instance(instance=movie, serializer_class=MovieSerializer)

        read_serializer = MovieSerializer(movie)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)
    
    @extend_schema(
        request=MovieCreateUpdateSerializer,
        responses={200: MovieSerializer},
        summary="Updating movie"
    )
    def update(self, request, pk=None) -> Response:
        movie = Movie.objects.get(pk=pk)
        serializer = MovieCreateUpdateSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.save()
        
        cache_model_instance(instance=movie, serializer_class=MovieSerializer)

        read_serializer = MovieSerializer(movie)
        return Response(read_serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        request=None,
        responses={204: None},
        summary="Delete movie",
        description="Delete an existing movie by ID"
    )
    def destroy(self, request, pk=None) -> Response:
        movie = Movie.objects.get(pk=pk)
        movie.delete()

        delete_cached_model(model_class=Movie, object_id=pk)

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @extend_schema(
        request=None,
        responses={200: MovieSerializer},
        summary="Retrieve movie",
        description="Get single movie by ID from cache"
    )
    def retrieve(self, request, pk=None) -> Response:
        cached = get_cached_model(model_class=Movie, object_id=pk)
        if cached:
            return Response(cached, status=status.HTTP_200_OK)

        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)

        cache_model_instance(instance=movie, serializer_class=MovieSerializer)

        return Response(serializer.data, status=status.HTTP_200_OK)