from rest_framework import serializers
from movies.models.models import Director

class DirectorCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["name"]

    def create(self, validated_data):
        director = Director.objects.create(**validated_data)
        return director

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
