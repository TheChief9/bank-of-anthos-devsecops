import jwt

def unsafe_decode(token):
    return jwt.decode(token, algorithms=["RS256"], options={"verify_signature": False})
