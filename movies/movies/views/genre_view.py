from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from movies.services.services import list_genres
from movies.serializers.serializers import GenreSerializer, GenreCreateUpdateSerializer
from movies.models.models import Genre


class GenreViewSet(viewsets.ViewSet):

    @extend_schema(
        request=None,
        responses={200: GenreSerializer(many=True)},
        summary="List genres",
        description="Returns list of all genres"
    )
    def list(self, request) -> Response:
        filters = {
            "name": request.query_params.get("name"),
        }
        queryset = list_genres(filters)
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=GenreCreateUpdateSerializer,
        responses={201: GenreSerializer},
        summary="Create genre"
    )
    def create(self, request) -> Response:
        serializer = GenreCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genre = serializer.save()
        read_serializer = GenreSerializer(genre)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=GenreCreateUpdateSerializer,
        responses={200: GenreSerializer},
        summary="Update genre"
    )
    def update(self, request, pk=None) -> Response:
        genre = Genre.objects.get(pk=pk)
        serializer = GenreCreateUpdateSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        genre = serializer.save()
        read_serializer = GenreSerializer(genre)
        return Response(read_serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=None,
        responses={204: None},
        summary="Delete genre",
        description="Deletes genre by ID"
    )
    def destroy(self, request, pk=None) -> Response:
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
