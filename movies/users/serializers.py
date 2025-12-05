from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        default="username",
        help_text="Username",
    )
    email = serializers.EmailField(
        default="user@example.com",
        help_text="Email"
    )
    password = serializers.CharField(
        write_only=True,
        default="12345678",
        help_text="Password"
    )
    
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)