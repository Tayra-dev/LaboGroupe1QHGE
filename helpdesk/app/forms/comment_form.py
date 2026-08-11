from flask_wtf import FlaskForm
from wtforms import HiddenField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    """Création d'un commentaire.
    """

    comment_content =  TextAreaField(
        "Commentaire",
        validators=[
            DataRequired(message="Le contenu du commentaire est obligatoire !")
        ]
    )

    # Champs cachés (Hidden) : invisibles pour l'utilisateur, mais lus par le Mapper
    author_id = HiddenField(
        "ID auteur",
        validators=[
            DataRequired(message="L'auteur est obligatoire !")
        ]
    )
    ticket_id = HiddenField(
        "ID ticket",
        validators=[
            DataRequired(message="Le ticket est obligatoire !")
        ]
    )