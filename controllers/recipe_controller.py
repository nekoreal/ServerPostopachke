from models.recipe import Recipe
from databasedir.database import db

def create_recipe(author_id, title='Без названия', description='Пусто', description_of_cooking_process='Пусто', rating=0.0, caloric_content=1, status_return:bool=False):
    db.session.add(Recipe(
        author_id=author_id,
        title=title,
        description=description,
        description_of_cooking_process=description_of_cooking_process,
        rating=rating,
        caloric_content=caloric_content
    ))
    db.session.commit()
    return ({'message': 'Рецепт создан'}, 201) if status_return else {'message': 'Рецепт создан'}

def get_all_recipes(status_return:bool=False, recursion:bool=False):
    '''
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    recipes = Recipe.query.all()
    res={"data":[recipe.to_dict(recursion=recursion) for recipe in recipes]}
    return (res, 200) if status_return else res

def get_recipe_by_id(recipe_id, dict:bool=True, status_return:bool=False,recursion:bool=False):
    '''
    :param recipe_id:
    :param dict=True: get dict
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    recipe = Recipe.query.get(recipe_id)
    res={'data':recipe.to_dict(recursion=recursion)} if dict else recipe
    if recipe:
        return (res, 200 ) if status_return else res
    else:
        return (None, 401) if status_return else None