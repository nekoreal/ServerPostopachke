from databasedir.database import db
#AT - associative table recipe ingrediennt


class Recipe_ingredient(db.Model):
    __tablename__ = 'recipe_ingredient'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id',ondelete="CASCADE"), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id',ondelete="CASCADE"), primary_key=True)
    amount = db.Column(db.String(50), default="Не указано")
    #AT associative table
    recipe = db.relationship("Recipe", back_populates="AT_recipe_ingredient")
    ingredient = db.relationship("Ingredient", back_populates="AT_recipe_ingredient")

    def __repr__(self):
        return (f'<Recipe {self.recipe_id}>'
                f'<Ingredient {self.ingredient_id}>'
                f'<amount {self.amount}>')