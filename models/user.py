from databasedir.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(80,collation='utf8mb4_bin' ), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False) #128 максимум для хэщ паролей
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_banned = db.Column(db.Boolean, nullable=False, default=False)

    recipes = db.relationship('Recipe', backref='author', lazy=True, cascade='all, delete-orphan')
    ratings = db.relationship('Rating', back_populates='author', cascade="all, delete-orphan")

    def get_recipes(self):
        return [recipe.to_dict() for recipe in self.recipes]

    def to_dict(self, recursion:bool=False):
        res={
            'id': self.id,
            'username': self.username,
            'is_admin': self.is_admin,
            'is_banned': self.is_banned,
        }
        if recursion: res.update({
            'recipes': [ recipe.to_dict() for recipe in self.recipes ]
        })
        return res

    def __repr__(self):
        return (f"({self.id} id) {self.username}\n"
                f"{'\n-----------------------\n'.join(list([ recipe.to_dict().__repr__() for recipe in self.recipes ]))}" )