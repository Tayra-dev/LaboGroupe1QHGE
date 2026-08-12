from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from app import app


DATA_REQUIRED_MSG = "Ce champ est requis"
LENGTH_MSG = "La longueur doit être comprise entre %(min)d et %(max)d caractères"
PASSWORD_VALIDATORS = (
    [
        DataRequired(message=DATA_REQUIRED_MSG),
        Length(
            4,
            25,
            message="Le mot de passe doit contenir entre %(min)d et %(max)d caractères",
        ),
        EqualTo("confirm", message="Les mots de passe encodés ne correspondent pas"),
    ]
    if app.debug
    else [
        DataRequired(message=DATA_REQUIRED_MSG),
        Length(
            12,
            80,
            message="Le mot de passe doit contenir entre %(min)d et %(max)d caractères",
        ),
        Regexp(
            r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!?(){}*$&@+=])",
            message="Le mot de passe doit contenir au moins une lettre minuscule, une majuscule, un chiffre et un caractère spécial : !?(){}*$&@+=",
        ),
    ]
)

class UserRegisterForm(FlaskForm):
    name = StringField(
        "Nom d'utilisateur",
        validators=[
            DataRequired(message=DATA_REQUIRED_MSG),
            Length(min=2, max=50, message=LENGTH_MSG),
        ],
    )
    email = EmailField(
        "Email",
        validators=[
            DataRequired(message=DATA_REQUIRED_MSG),
            Email("L'adresse email est requise pour l'inscription"),
        ],
    )
    password = PasswordField("Mot de passe", validators=PASSWORD_VALIDATORS)
    confirm = PasswordField("Confirmation du mot de passe")
    firstname = StringField(
        "Prénom",
        validators=[
            DataRequired(message=DATA_REQUIRED_MSG),
            Length(min=2, max=50, message=LENGTH_MSG),
        ],
    )
    lastname = StringField(
        "Nom de famille",
        validators=[
            DataRequired(message=DATA_REQUIRED_MSG),
            Length(min=2, max=50, message=LENGTH_MSG),
        ],
    )
