from flask import Blueprint,request,jsonify
from databasedir.database import db
from controllers import user_controller, recipe_controller

get_bp=Blueprint('get_bp', __name__)


@get_bp.route('/get_all_users', methods=['GET'])
def get_all_users_route():
    return jsonify(user_controller.get_all_users())

@get_bp.route('/get_all_recipes', methods=['GET'])
def get_all_recipes_route():
    return jsonify(recipe_controller.get_all_recipes())
