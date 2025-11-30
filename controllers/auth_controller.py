from models.user import User
from databasedir.database import db
from utils.hash_password import generate_password_hash, check_password_hash
from utils.tokens import generate_access_token
import re
from  utils.logger import logger


@logger('auth_controller.txt',
        printlog=True,
        time=True,
        only_exception=False)
def register_user(data):
    try:
        username = data.get('username')
        password = data.get('password')
    except:
        return {'message': 'Некорректные данные',"status_code":400}, 400

    if not username or not password or len(username) < 4 or len(password) <4 or len(username) > 20 or len(password) > 20 :
        return {'message': 'Некорректные данные. Длинна пароля или логина от 4 до 20',"status_code":400}, 400

    if (not re.search(r'[A-Za-z]', password) ) or (not re.search(r'\d', password)):
        return {'message': 'Некорректные данные. В пароле должны быть цифры и буквы',"status_code":400}, 400

    if User.query.filter_by(username=username).first():
        return {'message': 'Пользователь уже существует',"status_code":400}, 400

    password_hash = generate_password_hash(password)

    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    token = generate_access_token(identity=new_user.id)

    return { 'message':"Регистрация прошла успешна",'username': new_user.username, "token":token, "status_code":200}, 200


@logger('auth_controller.txt',
        printlog=True,
        time=True,
        only_exception=False)
def login_user(data):
    try:
        username = data.get('username')
        password = data.get('password')
    except:
        return {'message': 'Некорректные данные',"status_code":400}, 400

    current_user = User.query.filter_by(username=username).first()

    if not current_user:
        return {'message': 'Неправильный пароль или логин',"status_code":400}, 400

    if not check_password_hash(current_user.password_hash,password):
        return {'message': 'Неправильный пароль или логин',"status_code":400}, 400

    token = generate_access_token(identity=User.query.filter_by(username=username).first().id)


    return { 'message':"Авторизация прошла успешно",'username': current_user.username, "token": token, "status_code": 200}, 200
