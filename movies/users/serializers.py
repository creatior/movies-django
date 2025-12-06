from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        help_text="Username",
    )
    email = serializers.EmailField(
        required=True,
        help_text="Email"
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Password"
    )
    
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)