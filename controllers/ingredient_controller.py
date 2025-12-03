from databasedir.database import db
from models.ingredient import Ingredient

def create_ingredient(title:str="Пусто", description:str="Пусто", status_return:bool=False, *args, **kwargs):
    ingredient = db.session.query(Ingredient).filter(Ingredient.title == title).first()
    if ingredient:
        return ({'message': 'Ингредиент уже создан',"ingredient_id": ingredient.id }, 201) if status_return else {'message': 'Ингредиент уже создан',"ingredient_id": ingredient.id }
    ingredient = Ingredient(title=title, description=description)
    db.session.add(ingredient)
    db.session.commit()
    return ({'message': 'Ингредиент создан',"ingredient_id": ingredient.id }, 201) if status_return else {'message': 'Ингредиент создан',"ingredient_id": ingredient.id }

def get_all_ingredients(status_return:bool=False, recursion:bool=False, *args, **kwargs):
    '''
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    ingredients = Ingredient.query.all()
    res = {"data": [ingredient.to_dict(recursion=recursion) for ingredient in ingredients]}
    return (res, 200) if status_return else res

def get_ingredient_by_id(ingredient_id, dict:bool=True, status_return:bool=False,recursion:bool=False, *args, **kwargs):
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