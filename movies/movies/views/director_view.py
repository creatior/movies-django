from rest_framework import status
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from movies.serializers.serializers import DirectorSerializer, DirectorCreateUpdateSerializer
from movies.services.services import list_directors
from movies.models.director import Director
from movies.views.base_movie_view import BaseMovieViewSet

class DirectorViewSet(BaseMovieViewSet):
    @extend_schema(
        request=None,
        responses={200: DirectorSerializer(many=True)},
        summary="List directors",
        description="Returns list of all directors"
    )
    def list(self, request) -> Response:
        filters = {
            "full_name": request.query_params.get("full_name"),
        }
        queryset = list_directors(filters)
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=DirectorCreateUpdateSerializer,
        responses={201: DirectorSerializer},
        summary="Create director"
    )
    def create(self, request) -> Response:
        serializer = DirectorCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director = serializer.save()
        read_serializer = DirectorSerializer(director)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=DirectorCreateUpdateSerializer,
        responses={200: DirectorSerializer},
        summary="Update director"
    )
    def update(self, request, pk=None) -> Response:
        director = Director.objects.get(pk=pk)
        serializer = DirectorCreateUpdateSerializer(director, data=request.data)
        serializer.is_valid(raise_exception=True)
        director = serializer.save()
        read_serializer = DirectorSerializer(director)
        return Response(read_serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=None,
        responses={204: None},
        summary="Delete director",
        description="Deletes director by ID"
    )
    def destroy(self, request, pk=None) -> Response:
        director = Director.objects.get(pk=pk)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
