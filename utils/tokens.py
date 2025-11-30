from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from utils.logger import logger

jwt = JWTManager()

@logger(txtfile="inits.txt", printlog=True, raiseexc=True, time=True)
def init_jwt(app):
    jwt.init_app(app)

def generate_access_token(identity):
    identity = str(identity)
    return create_access_token(identity=identity, expires_delta=False)
