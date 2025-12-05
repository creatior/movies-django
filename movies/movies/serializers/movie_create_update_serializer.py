from rest_framework import serializers
from movies.models.models import Movie, Genre, Director

class MovieCreateUpdateSerializer(serializers.ModelSerializer):
    genre_ids = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, write_only=True)
    director_id = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all(), write_only=True)

    class Meta:
        model = Movie
        fields = ["title", "description", "release_year", "genre_ids", "director_id"]

    def create(self, validated_data):
        genres = validated_data.pop("genre_ids", [])
        director = validated_data.pop("director_id")
        movie = Movie.objects.create(director=director, **validated_data)
        movie.genres.set(genres)
        return movie

    def update(self, instance, validated_data):
        genres = validated_data.pop("genres_ids", None)
        director = validated_data.pop("director_id", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if director:
            instance.director = director
        instance.save()
        if genres is not None:
            instance.genres.set(genres)
        return instance
