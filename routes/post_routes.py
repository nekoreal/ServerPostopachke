from flask import Blueprint,request,jsonify

from controllers import user_controller, auth_controller

post_bp=Blueprint('post_bp', __name__)


@post_bp.route('/register_user', methods=['POST'])
def register_user_route():
    return auth_controller.register_user(request.form)

@post_bp.route('/login_user', methods=['POST'])
def login_user_route():
    return auth_controller.login_user(request.form)

@post_bp.route('/test', methods=['POST'])
def test():
    print(request.form)
    return 'Да была'
