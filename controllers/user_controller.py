from models.user import User
from databasedir.database import db
from utils.hash_password import generate_password_hash, check_password_hash
from utils.tokens import generate_access_token


def create_user(username: str, password: str):
    if User.query.filter_by(username=username).first():
        return {'error': 'Пользователь уже существует'}, 400
    db.session.add(User(
        username=username,
        password_hash=generate_password_hash(password)
    ))
    db.session.commit()
    return {'message': 'Пользователь создан'}, 201

def get_all_users():
    users = User.query.all()
    return {"data":[user.to_dict() for user in users]}, 200


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return user.to_dict(),200
    else:
        return None, 401