from flask import Blueprint,request,jsonify
from sqlalchemy import text #для сырых запросов текстом пример: result = db.session.execute(text("update user set is_admin=True where username='admin';"))
from databasedir.database import db
from controllers import user_controller, recipe_controller
from models.ingredient import Ingredient,Recipe_ingredient
from models.recipe import Recipe
from models.user import User
from controllers.auth_controller import register_user

get_bp=Blueprint('get_bp', __name__)


@get_bp.route('/get_all_users', methods=['GET'])
def get_all_users_route():
    return jsonify(user_controller.get_all_users(recursion=True))

@get_bp.route('/get_all_recipes', methods=['GET'])
def get_all_recipes_route():
    return jsonify(recipe_controller.get_all_recipes(recursion=True))
