from rest_framework import serializers
from movies.models.models import Director

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "name"]
