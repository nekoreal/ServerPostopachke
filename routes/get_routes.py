from flask import Blueprint,request,jsonify
import controllers.user_controller
from controllers import user_controller

get_bp=Blueprint('get_bp', __name__)


@get_bp.route('/get_all_users', methods=['GET'])
def get_all_users_route():
    return jsonify(user_controller.get_all_users())
