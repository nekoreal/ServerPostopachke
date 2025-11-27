from databasedir.database import db
from models.at_recipe_ingredient import Recipe_ingredient

def create_recipe_ingredient(recipe_id, ingredient_id, amount:str="0", status_return:bool=False):
    db.session.add(Recipe_ingredient(recipe_id=recipe_id, ingredient_id=ingredient_id, amount=amount))
    db.session.commit()
    return ({'message': 'Рецепт создан'}, 201) if status_return else {'message': 'Рецепт создан'}