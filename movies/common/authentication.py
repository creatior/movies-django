from rest_framework import authentication, exceptions
from django.contrib.auth import get_user_model
from .auth import decode_jwt

User = get_user_model()

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None  # DRF попробует другие аутентификаторы или вернёт 401

        try:
            prefix, token = auth_header.split(" ")
            if prefix.lower() != "bearer":
                raise exceptions.AuthenticationFailed("Invalid token prefix")
        except ValueError:
            raise exceptions.AuthenticationFailed("Invalid authorization header")

        try:
            payload = decode_jwt(token)
        except Exception:
            raise exceptions.AuthenticationFailed("Invalid or expired token")

        try:
            user = User.objects.get(id=payload["user_id"])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User not found")

        return (user, None)
