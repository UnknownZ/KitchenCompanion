from models import db
from models.relations import ingredient_user
from models.ingredient import Ingredient

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(120))
    allergies = db.relationship("Ingredient", secondary="ingredient_user")

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
            
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "user": self.name,
            "email": self.email,
        }

    def serialize_with_ingredient(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "ingredient": self.get_allergies()
        }

    def get_allergies(self):
        return list(map(lambda ingredient: ingredient.serialize(), self.allergies))