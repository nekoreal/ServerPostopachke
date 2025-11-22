from models.recipe import Recipe
from databasedir.database import db

def create_recipe(author_id, title='Без названия', description='', description_of_cooking_process='', rating=0.0, caloric_content=1, status_return:bool=False):
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

def get_all_recipes(status_return:bool=False):
    recipes = Recipe.query.all()
    return ({"data":[recipe.to_dict() for recipe in recipes]}, 200) if status_return else {"data":[recipe.to_dict() for recipe in recipes]}

def get_recipe_by_id(recipe_id, dict:bool=True, status_return:bool=False):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        return (({'data':recipe.to_dict()} if dict else recipe, 200 )) if status_return else ({'data':recipe.to_dict()} if dict else recipe)
    else:
        return (None, 401) if status_return else None