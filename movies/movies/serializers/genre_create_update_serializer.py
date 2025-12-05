from rest_framework import serializers
from movies.models.models import Genre

class GenreCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]

    def create(self, validated_data):
        genre = Genre.objects.create(**validated_data)
        return genre

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
