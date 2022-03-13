import jwt


def encode_jwt(headers, payload, secret):
    token = jwt.encode(payload=payload, key=secret, headers=headers, algorithm="HS256")
    return token


def verify_token(encoded, key=None, algorithms=["HS256"]):
    try:
        data = jwt.decode(encoded, key=key, algorithms=algorithms)
    except jwt.exceptions.InvalidSignatureError:
        return None
    return data
