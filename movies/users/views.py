from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer, LoginSerializer
from .services import register_user, login_user
from drf_spectacular.utils import extend_schema

class UserViewSet(viewsets.ViewSet):
    
    @extend_schema(
        request=RegistrationSerializer,
        responses={201: RegistrationSerializer},
        summary="New user registration",
        description="Creates user and returns JWT"
    )
    @action(
        detail=False, 
        methods=["post"],
        authentication_classes=[],
        permission_classes=[AllowAny]
        )
    def register(self, request) -> Response:
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = register_user(serializer.validated_data)
        return Response({"user_id" : user.id, "token": token}, status=status.HTTP_201_CREATED)
    
    @extend_schema(
        request=LoginSerializer,
        responses={200: LoginSerializer},
        summary="Login",
        description="Login and returns JWT"
    )
    @action(
        detail=False, 
        methods=["post"],
        authentication_classes=[],
        permission_classes=[AllowAny]
    )
    def login(self, request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = login_user(serializer.validated_data['username'], serializer.validated_data['password'])
        return Response({"token": token}, status=status.HTTP_200_OK)

