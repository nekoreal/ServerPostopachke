from flask import Blueprint,request,jsonify, send_file
from models.recipe import Recipe
from controllers import user_controller, auth_controller, avatar_controller
from io import BytesIO
from PIL import Image
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.logger import logger

post_bp=Blueprint('post_bp', __name__)


@post_bp.route('/register_user', methods=['POST'])
def register_user_route():
    return auth_controller.register_user(request.form)

@post_bp.route('/login_user', methods=['POST'])
def login_user_route():
    return auth_controller.login_user(request.form)

@post_bp.route('/set_avatar', methods=['POST'])
@jwt_required()
def upload_image():
    return avatar_controller.save_avatar(Image.open(request.files['photo'].stream), get_jwt_identity())
