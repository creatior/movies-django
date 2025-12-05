from rest_framework import viewsets, status
from rest_framework.response import Response
from movies.serializers.serializers import MovieSerializer, MovieCreateUpdateSerializer
from movies.services.services import list_movies
from movies.models.models import Movie
from drf_spectacular.utils import extend_schema

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
        return Response(status=status.HTTP_204_NO_CONTENT)