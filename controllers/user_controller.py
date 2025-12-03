from models.user import User
from databasedir.database import db
from utils.hash_password import generate_password_hash, check_password_hash
from utils.tokens import generate_access_token


def create_user(username: str, password: str, status_return:bool=False,*args, **kwargs):
    if User.query.filter_by(username=username).first():
        return {'error': 'Пользователь уже существует'}, 400 if status_return else {'error': 'Пользователь уже существует'}
    db.session.add(User(
        username=username,
        password_hash=generate_password_hash(password)
    ))
    db.session.commit()
    return ({'message': 'Пользователь создан'}, 201)  if status_return else {'message': 'Пользователь создан'}

def get_all_users(status_return:bool=False, recursion:bool=False,*args, **kwargs):
    '''
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    users = User.query.all()
    res={"data":[user.to_dict(recursion=recursion) for user in users]}
    return ( res, 200) if status_return else res


def get_user_by_id(user_id,dict:bool=True, status_return:bool=False, recursion:bool=False, *args, **kwargs):
    '''
    :param user_id:
    :param dict=True: get dict
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    user = User.query.get(user_id)
    res = {'data':user.to_dict(recursion=recursion)} if dict else user
    if user:
        return (res ,200 )if status_return else res
    else:
        return None, 401 if status_return else None


def get_user_recipes_by_id(user_id, dict:bool=True, status_return:bool=False, recursion:bool=False, *args, **kwargs):
    current_user  = get_user_by_id(user_id, dict=False)
    res = {"data": [ recipe.to_dict(recursion=recursion) for recipe in current_user.recipes] if dict else current_user.recipes }
    return (res ,200 )if status_return else res

def get_user_ratings_by_id(user_id, dict:bool=True, status_return:bool=False, recursion:bool=False, *args, **kwargs):
    current_user  = get_user_by_id(user_id, dict=False)
    res = {"data": [ rating.to_dict(recursion=recursion) for rating in current_user.ratings] if dict else current_user.ratings }
    return (res ,200 )if status_return else res
