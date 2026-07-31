from app import db
from app.models.base_entity import BaseEntity


class KnowledgeArticle(BaseEntity, db.Model):
    """Un article de la base de connaissances"""

    __tablename__ = "knowledgearticles"

    article_id = db.Column("articleid", db.Integer, primary_key=True, autoincrement=True)
    title = db.Column("articletitle", db.String(100))
    content = db.Column("articlecontent", db.Text)

    category_id = db.Column("categoryid", db.ForeignKey("categories.categoryid"))
    author_id = db.Column("authorid", db.ForeignKey("users.userid"))

    category = db.relationship("Category", back_populates="knowledgearticles")
    author = db.relationship("Author", back_populates="knowledgearticles")

    def __repr__(self):
        return f"<Article {self.article_id}: {self.title}>"