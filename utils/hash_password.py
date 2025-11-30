from flask_bcrypt import Bcrypt
from utils.logger import logger

bcrypt = Bcrypt()


@logger(txtfile="inits.txt", printlog=True, raiseexc=True, time=True)
def init_bcrypt(app):
    bcrypt.init_app(app)

def generate_password_hash(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password_hash(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)
