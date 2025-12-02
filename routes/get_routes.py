from flask import Blueprint,request,jsonify, send_file, abort
from sqlalchemy import text #для сырых запросов текстом пример: result = db.session.execute(text("update user set is_admin=True where username='admin';"))
from sqlalchemy.sql.functions import current_user
from io import BytesIO
from databasedir.database import db
from controllers import user_controller, recipe_controller, ingredient_controller, at_recipe_ingredient_controller, auth_controller, avatar_controller, rating_controller

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.rating import Rating
from utils.logger import logger

from models.recipe import Recipe
from models.user import User
from models.ingredient import Ingredient
from models.at_recipe_ingredient import Recipe_ingredient

from miniIO_S3.S3photos import get_photo_bytes

get_bp=Blueprint('get_bp', __name__)


@get_bp.route('/get_all_users', methods=['GET'])
def get_all_users_route():
    return jsonify(user_controller.get_all_users(recursion=True))

@get_bp.route('/get_all_recipes', methods=['GET'])
def get_all_recipes_route():
    return jsonify(recipe_controller.get_all_recipes(recursion=True))

@get_bp.route('/get_all_ingredients', methods=['GET'])
def get_all_ingredients_route():
    return jsonify(ingredient_controller.get_all_ingredients(recursion=True))

@get_bp.route('/get_all_ratings', methods=['GET'])
def get_all_ratings_route():
    return jsonify(rating_controller.get_all_ratings(recursion=True))

@get_bp.route('/get_my_recipes', methods=['GET'])
@jwt_required()
def get_my_recipes_route():
    return jsonify(user_controller.get_user_recipes_by_id(int(get_jwt_identity())))


@get_bp.route('/get_my_ratings', methods=['GET'])
@jwt_required()
def get_my_ratings_route():
    return jsonify(user_controller.get_user_ratings_by_id(int(get_jwt_identity()), recursion=True))

@get_bp.route('/get_my_avatar', methods=['GET'])
@jwt_required()
def get_my_avatar_route():
    avatar_bytes = avatar_controller.get_avatar_bytes(get_jwt_identity())
    if not avatar_bytes:
        return jsonify({"error": "Avatar not found"}), 404
    return send_file(
        BytesIO(avatar_bytes),
        mimetype='image/jpeg',
        as_attachment=False,
        download_name=f'{get_jwt_identity()}.jpg'
    )