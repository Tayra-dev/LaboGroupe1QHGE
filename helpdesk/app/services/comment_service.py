from app import db, app
from app.services.base_service import BaseService
from app.models.comment import Comment
from app.mappers.comment_mapper import CommentMapper

class CommentService(BaseService):

    def find_all(self):
        """Tous les commentaires (sous forme de DTO)."""
        try:
            comments = Comment.query.all()

            return [CommentMapper.entity_to_dto(comment) for comment in comments]

        except Exception as e:
            app.logger.error(f"Error | find_all comments: {e}")
            return None
            # db.session.rollback() pas nécessaire car juste un appel à la db

    def find_one(self, entity_id: int):
        """Un commentaire par sa clé primaire, ou None."""
        try:
            comment = db.session.get(Comment, entity_id)

            if comment is None:
                return None
            
            return CommentMapper.entity_to_dto(comment)

        except Exception as e:
            app.logger.error(f"Error | find_one comment: {e}")
            return None
            # db.session.rollback() pas nécessaire car juste un appel à la db

    def find_one_by(self, **kwargs):
        """Un commentaire par n'importe quelle colonne: find_one_by(username='x')."""
        try:
            comment = Comment.query.filter_by(**kwargs).one_or_none()

            if comment is None:
                return None

            return CommentMapper.entity_to_dto(comment)

        except Exception as e:
            app.logger.error(f"Error | find_one_by comment: {e}")
            return None
            # db.session.rollback() pas nécessaire car juste un appel à la db


    def insert(self, data):
        """Crée un commentaire à partir d'un formulaire validé."""
        try:
            form = data['form']
            author_id = data['author_id']
            ticket_id = data['ticket_id']

            comment = Comment()

            comment = CommentMapper.form_to_entity(
                form, 
                comment, 
                author_id, 
                ticket_id)

            db.session.add(comment)
            db.session.commit()

            return CommentMapper.entity_to_dto(comment)

        except Exception as e:
            app.logger.error(f"Error | insert comment: {e}")
            db.session.rollback()
            return None            


    def update(self, entity_id: int, data):
        """Met à jour un commentaire existant."""

    def delete(self, entity_id: int):
        """Supprime un commentaire."""