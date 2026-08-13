from app.framework.mapper.abstract_mapper import AbstractMapper
<<<<<<< HEAD
from dtos.comment_dto import CommentDTO
from models.comment import Comment
from forms.comment_form import CommentForm
=======
from app.dtos.comment_dto import CommentDTO
from app.models.comment import Comment
from app.forms.comment_form import CommentForm
>>>>>>> devC/controller

class CommentMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(comment: Comment) -> CommentDTO:
        return CommentDTO.build_from_entity(comment)

    @staticmethod
    def form_to_entity(form, comment: Comment, author_id: int, ticket_id: int) -> Comment:
        if isinstance(form, CommentForm):
            comment.comment_content = form.comment_content.data
            comment.author_id = author_id
            comment.ticket_id = ticket_id
        return comment


  