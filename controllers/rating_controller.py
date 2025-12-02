from models.rating import Rating
from databasedir.database import db

def set_rating(author_id, recipe_id, rating:int|str=5, status_return:bool=False):
    rating = int(rating)
    existing_rating = Rating.query.filter_by(author_id=author_id, recipe_id=recipe_id).first()
    if existing_rating:
        existing_rating.rating = rating
        db.session.commit()
        return ({'message': 'Оценка изменена'}, 201) if status_return else {'message': 'Оценка изменена'}
    else:
        rating = Rating(author_id=author_id, recipe_id=recipe_id, rating=rating)
        db.session.add(rating)
        db.session.commit()
        return ({'message': 'Оценка создана'}, 201) if status_return else {'message': 'Оценка создана'}

def delete_rating(author_id, recipe_id,  status_return:bool=False):
    existing_rating:Rating = Rating.query.filter_by(author_id=author_id, recipe_id=recipe_id).first()
    if existing_rating:
        db.session.delete(existing_rating)
        db.session.commit()
        return ({'message': 'Оценка изменена'}, 201) if status_return else {'message': 'Оценка изменена'}
    else:
        return ({'message': 'Оценка не найдена'}, 404) if status_return else {'message': 'Оценка не найдена'}



def get_all_ratings(status_return:bool=False, recursion:bool=False):
    '''
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    ratings = Rating.query.all()
    res={"data":[rating.to_dict(recursion=recursion) for rating in ratings]}
    return (res, 200) if status_return else res

def get_user_ratings_by_id(user_id, dict:bool=True, status_return:bool=False):
    current_user  = get_user_by_id(user_id, dict=False)
    res = {"data": [ recipe.to_dict() for recipe in current_user.recipes] if dict else current_user.recipes }
    return (res ,200 )if status_return else res