from .models import User
from common.auth import encode_jwt

def register_user(data):
    user = User.objects.create_user(**data)
    token = encode_jwt(user)
    return user, token

def login_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise Exception("Invalid credentials")
    
    if user.check_password(password):
        token = encode_jwt(user)
        return token
    raise Exception("Invalid credentials")