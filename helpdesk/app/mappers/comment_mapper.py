from app.mappers.abstract_mapper import AbstractMapper
from dtos.comment_dto import CommentDTO
from models.comment import Comment
from forms.comment_form import CommentForm

class CommentMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(comment: Comment) -> CommentDTO:
        return CommentDTO.build_from_entity(comment)

    @staticmethod
    def form_to_entity(form, comment: Comment) -> Comment:
        if isinstance(form, CommentForm):
            comment.comment_content = form.comment_content.data
            comment.author_id = form.author_id.data
            comment.ticket_id = form.ticket_id.data
        return comment


  