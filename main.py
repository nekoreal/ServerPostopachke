from flask import Flask
from flask_cors import CORS
from config import Config
from models import ingredient

from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.at_recipe_ingredient import Recipe_ingredient
#Это нужно, чтобы sqlachery увидел их

app = Flask(__name__)
app.config.from_object(Config) #Сразу вбивает данные с config.py ключи, пароли и тд

CORS(app)

from databasedir.database import init_db, db
init_db(app)

from utils.tokens import init_jwt
init_jwt(app)

from utils.hash_password import init_bcrypt
init_bcrypt(app)


#регистрация blueprintov с файлов где были созданы blueprint'ы
from routes import get_routes, post_routes
app.register_blueprint(get_routes.get_bp)
app.register_blueprint(post_routes.post_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    app.run(debug=True,host="0.0.0.0", port=5001)

