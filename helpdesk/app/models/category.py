from app import db
from app.models.base_entity import BaseEntity

# Used to categorize tickets.
class Category(BaseEntity, db.Model):

    __tablename__ = "categories"

    category_id = db.Column("categoryid", db.Integer, primary_key=True)
    name = db.Column("categoryname", db.text, nullable=False, index=True, unique=true)
    description = db.Column("categorydescription", db.String(255), nullable=False)

    def __repr__(self):
        return f"<Category ['{self.name}' ID: {self.category_id}]>"