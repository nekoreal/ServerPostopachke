from databasedir.database import db


class Rating(db.Model):
    __table_args__ = (
        db.UniqueConstraint('author_id', 'recipe_id', name='unique_author_recipe'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id', ondelete="CASCADE"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    author = db.relationship('User', back_populates='ratings')
    recipe = db.relationship('Recipe', back_populates='ratings')


    def to_dict(self,recursion:bool=False):
        res={
            'author_id': self.author_id,
            'recipe_id': self.recipe_id,
            'rating': self.rating
        }
        if recursion: res.update({
            'author': self.author.to_dict(),
            'recipe': self.recipe.to_dict(),
        })
        return res

    def __repr__(self):
        return (f"<author({self.author_id}) recipe({self.recipe_id})>\n" 
                f"{self.rating}\n" )

