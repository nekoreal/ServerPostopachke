from databasedir.database import db
from models.recipe_ingredient import Recipe_ingredient


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(80), nullable=False, default='Пусто', unique=True)
    description = db.Column(db.Text, nullable=False, default='Пусто')
    # AT associative table
    AT_recipe_ingredient = db.relationship(Recipe_ingredient, back_populates="ingredient",cascade='all, delete-orphan')

    def to_dict(self,amount='Не указано',recursion:bool=False):
        res={
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'amount':amount,
        }
        if recursion: res.update({
            "recipes": [ AT.recipes.to_dict() for AT in self.AT_recipe_ingredient ],
        })
        return res

    def __repr__(self):
        return (f"id: {self.id}, title: {self.title}, description: {self.description}")

