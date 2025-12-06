from .models import User
from common.auth import encode_jwt
from django.db import IntegrityError

def register_user(data):
    try:
        user = User.objects.create_user(**data)
    except IntegrityError:
        raise ValueError("Username or email already exists")
    token = encode_jwt(user)
    return user, token

def login_user(username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Exception("Invalid credentials")
    
    if user.check_password(password):
        token = encode_jwt(user)
        return token
    raise Exception("Invalid credentials")