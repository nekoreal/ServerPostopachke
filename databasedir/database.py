from flask_sqlalchemy import SQLAlchemy

db:SQLAlchemy = SQLAlchemy()

def init_db(app):
    db.init_app(app)
