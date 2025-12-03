from databasedir.database import db
from models.at_recipe_ingredient import Recipe_ingredient
from controllers.ingredient_controller import create_ingredient


def create_recipe_ingredient(recipe_id, ingredient_title, amount:str|int="0", status_return:bool=False, *args, **kwargs):
    amount = str(amount)
    ingredient_id = create_ingredient(ingredient_title)['ingredient_id']
    db.session.add(Recipe_ingredient(recipe_id=recipe_id, ingredient_id=ingredient_id, amount=amount))
    db.session.commit()
    return ({'message': 'Связь создана'}, 201) if status_return else {'message': 'Связь создана'}

def create_recipe_ingredient_by_id(recipe_id, ingredient_id, amount:str="0", status_return:bool=False, *args, **kwargs):
    db.session.add(Recipe_ingredient(recipe_id=recipe_id, ingredient_id=ingredient_id, amount=amount))
    db.session.commit()
    return ({'message': 'Связь создана'}, 201) if status_return else {'message': 'Связь создана'}