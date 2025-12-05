from rest_framework import serializers
from movies.models.models import Movie
from .genre_serializer import GenreSerializer
from .director_serializer import DirectorSerializer

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "release_year", "genres", "director"]
