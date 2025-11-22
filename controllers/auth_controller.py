from models.user import User
from databasedir.database import db
from utils.hash_password import generate_password_hash, check_password_hash
from utils.tokens import generate_access_token



def register_user(data):
    try:
        username = data.get('username')
        password = data.get('password')
    except:
        return {'error': 'Некорректные данные'}, 400

    if not username or not password or len(username) < 3 or len(password) < 4:
        return {'error': 'Некорректные данные'}, 400

    if User.query.filter_by(username=username).first():
        return {'error': 'Пользователь уже существует'}, 409

    password_hash = generate_password_hash(password)

    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    token = generate_access_token(identity=new_user.id)

    return {'username': new_user.username, "token":token}, 201

def login_user(data):
    try:
        username = data.get('username')
        password = data.get('password')
    except:
        return {'error': 'Некорректные данные'}, 400

    current_user = User.query.filter_by(username=username).first()
    if not check_password_hash(current_user.password_hash,password):
        return {'message': 'Неправильный пароль или логин'}, 401

    token = generate_access_token(identity=User.query.filter_by(username=username).first().id)
    return {'username': current_user.username, "token":token}, 201
