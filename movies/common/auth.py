import jwt
from django.conf import settings
from datetime import datetime, timedelta

def encode_jwt(user):
    payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

def decode_jwt(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
