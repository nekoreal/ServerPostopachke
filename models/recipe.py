from databasedir.database import db
from models.rating import Rating


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(80), nullable=False, default='Пусто')
    description = db.Column(db.Text, nullable=False, default='Пусто')
    description_of_cooking_process = db.Column(db.Text, nullable=False, default='Пусто')
    caloric_content = db.Column(db.Integer, nullable=False, default=0)

    ratings = db.relationship('Rating', back_populates='recipe', cascade="all, delete-orphan", lazy='dynamic') #dynamic чтобы в avg полули не список , а запрос для дальнейших действий

    # AT associative table
    AT_recipe_ingredient = db.relationship("Recipe_ingredient", back_populates="recipe",cascade='all, delete-orphan')

    def to_dict(self,recursion:bool=False):
        res={
            'id': self.id,
            'author_id': self.author_id,
            'title': self.title,
            'description': self.description,
            'description_of_cooking_process': self.description_of_cooking_process,
            'rating': self.avg_rating,
            'caloric_content': self.caloric_content,
            'ingredients': [AT.ingredient.to_dict(amount=AT.amount) for AT in self.AT_recipe_ingredient],
        }
        if recursion: res.update({
            'author': self.author.to_dict(),
            'ratings': [rating.to_dict() for rating in self.ratings],
        })
        return res

    def __repr__(self):
        return (f"<({self.id}) {self.title}>\n" 
                f"{self.title}\n"
                f"{self.description}\n"
                f"{self.description}\n")

    @property
    def avg_rating(self):
        ratings = self.ratings.with_entities(db.func.avg(Rating.rating)).scalar() #Что бы работало lazy = dynamic
        return round(ratings, 1) if ratings else "0"


