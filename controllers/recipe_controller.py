from models.recipe import Recipe
from controllers.at_recipe_ingredient_controller import create_recipe_ingredient
from databasedir.database import db

def create_recipe_with_ingredients(
        author_id,
        title='Без названия',
        description='Пусто',
        description_of_cooking_process='Пусто',
        caloric_content=1,
        ingredients=None,
        status_return:bool=False,
        *args, **kwargs
):
    if ingredients is None:
        ingredients = {}
    recipe = Recipe(author_id=author_id,
                    title=title,
                    description=description,
                    description_of_cooking_process=description_of_cooking_process,
                    caloric_content=caloric_content,
                    )
    db.session.add(recipe)
    db.session.commit()
    for ingredient_title, amount in ingredients.items():
        create_recipe_ingredient(recipe.id, ingredient_title, amount=amount)
    return ({'message': 'Рецепт создан'}, 201) if status_return else {'message': 'Рецепт создан'}

def edit_recipe(
        author_id,
        recipe_id,
        title=None,
        description=None,
        description_of_cooking_process=None,
        caloric_content=None,
        ingredients=None,
        status_return:bool=False,
        *args, **kwargs
):
    recipe = db.session.query(Recipe).filter_by(id=recipe_id).first()
    if str(recipe.author_id) != str(author_id):
        return ({'message': 'Рецепт не ваш'}, 201) if status_return else {'message': 'Рецепт не ваш'}
    if not(title is None) : recipe.title = title
    if not(description is None) : recipe.description = description
    if not(description_of_cooking_process is None) : recipe.description_of_cooking_process = description_of_cooking_process
    if not(caloric_content is None) : recipe.caloric_content = caloric_content
    if not(ingredients is None) :
        for AT in recipe.AT_recipe_ingredient:
            db.session.delete(AT.ingredient)
        db.session.commit()
        for ingredient_title, amount in ingredients.items():
            create_recipe_ingredient(recipe.id, ingredient_title, amount=amount)
    db.session.commit()
    return ({'message': 'Рецепт изменен'}, 201) if status_return else {'message': 'Рецепт изменен'}

def create_recipe(
        author_id,
        title='Без названия',
        description='Пусто',
        description_of_cooking_process='Пусто',
        caloric_content=1,
        status_return:bool=False,
        *args, **kwargs
):
    db.session.add(Recipe(
        author_id=author_id,
        title=title,
        description=description,
        description_of_cooking_process=description_of_cooking_process,
        caloric_content=caloric_content
    ))
    db.session.commit()
    return ({'message': 'Рецепт создан'}, 201) if status_return else {'message': 'Рецепт создан'}

def get_all_recipes(
        status_return:bool=False,
        recursion:bool=False,
        *args, **kwargs
):
    '''
    :param status_return=False: get status code
    :param recursion=False:
    :return:
    '''
    recipes = Recipe.query.all()
    res={"data":[recipe.to_dict(recursion=recursion) for recipe in recipes]}
    return (res, 200) if status_return else res

def get_recipe_by_id(
        recipe_id,
        dict:bool=True,
        status_return:bool=False,
        recursion:bool=False,
        *args, **kwargs
):
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