from flask_sqlalchemy import SQLAlchemy
from utils.logger import logger

db:SQLAlchemy = SQLAlchemy()

@logger(txtfile="inits.txt", printlog=True, raiseexc=True, time=True)
def init_db(app):
    db.init_app(app)
