from app import db
from app.models.base_entity import BaseEntity

class Comment(BaseEntity, db.Model):

    """Commentaire publié sur un ticket."""

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    comment_content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id'), nullable=False)

    #Relations

    author = db.relationship('User', back_populates='comments')
    ticket = db.relationship('Ticket', back_populates='comments')

    def __repr__(self):
        return f"<Comment {self.comment_id}>"