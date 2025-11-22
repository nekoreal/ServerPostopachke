from databasedir.database import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    description_of_cooking_process = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    caloric_content = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<({self.id}) {self.title}>"