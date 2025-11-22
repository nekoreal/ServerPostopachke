from databasedir.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_banned = db.Column(db.Boolean, nullable=False, default=False)

    recipes = db.relationship('Recipe', backref='author', lazy=True, cascade='all, delete-orphan')

    def get_recipes(self):
        return [recipe.to_dict() for recipe in self.recipes]

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password_hash': self.password_hash,
            'is_admin': self.is_admin,
            'is_banned': self.is_banned,
            'recipes': [ recipe.to_dict() for recipe in self.recipes ],
        }

    def __repr__(self):
        return (f"({self.id} id) {self.username}\n"
                f"{'\n-----------------------\n'.join(list([ recipe.to_dict().__repr__() for recipe in self.recipes ]))}" )