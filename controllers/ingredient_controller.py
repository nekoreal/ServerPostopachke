from databasedir.database import db
from models.ingredient import Ingredient

def create_ingredient(title:str="Пусто", description:str="Пусто", status_return:bool=False):
    db.session.add(Ingredient(title=title, description=description))
    db.session.commit()
    return ({'message': 'Ингредиент создан'}, 201) if status_return else {'message': 'Рецепт создан'}

def get_all_ingredients(status_return:bool=False, recursion:bool=False):
    '''
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    ingredients = Ingredient.query.all()
    res = {"data": [ingredient.to_dict(recursion=recursion) for ingredient in ingredients]}
    return (res, 200) if status_return else res

def get_ingredient_by_id(ingredient_id, dict:bool=True, status_return:bool=False,recursion:bool=False):
    '''
    :param recipe_id:
    :param dict=True: get dict
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    ingredient = Ingredient.query.get(ingredient_id)
    res={'data':ingredient.to_dict(recursion=recursion)} if dict else ingredient
    if ingredient:
        return (res, 200 ) if status_return else res
    else:
        return (None, 401) if status_return else None