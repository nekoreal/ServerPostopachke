from models.user import User
from databasedir.database import db
from utils.hash_password import generate_password_hash, check_password_hash
from utils.tokens import generate_access_token


def create_user(username: str, password: str, status_return:bool=False):
    if User.query.filter_by(username=username).first():
        return {'error': 'Пользователь уже существует'}, 400 if status_return else {'error': 'Пользователь уже существует'}
    db.session.add(User(
        username=username,
        password_hash=generate_password_hash(password)
    ))
    db.session.commit()
    return ({'message': 'Пользователь создан'}, 201)  if status_return else {'message': 'Пользователь создан'}

def get_all_users(status_return:bool=False):
    users = User.query.all()
    return ({"data":[user.to_dict() for user in users]}, 200) if status_return else {"data":[user.to_dict() for user in users]}


def get_user_by_id(user_id,dict:bool=True, status_return:bool=False):
    user = User.query.get(user_id)
    if user:
        return (({"data":user.to_dict()} if dict else user) ,200 )if status_return else {"data":user.to_dict()} if dict else user
    else:
        return None, 401 if status_return else None