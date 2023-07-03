from models import db

class Ingredient(db.Model):
    __tablename__='ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    food_groups_id = db.Column(db.Integer, db.ForeignKey('food_groups.id'), nullable=False)
    #users = db.relationship("User", secondary="ingredient_user", back_populates="ingredients")
    #recipes = db.relationship("Recipes", secondary="ingredient_recipe", back_populates="ingredients")

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
            "name": self.name,
            
        }

    def serialize_with_group(self):
        return {
            "id": self.id,
            "name": self.name,
            "food_group": self.group.name
        }