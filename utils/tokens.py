from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

jwt = JWTManager()

def init_jwt(app):
    jwt.init_app(app)

def generate_access_token(identity):
    identity = str(identity)
    return create_access_token(identity=identity, expires_delta=False)
