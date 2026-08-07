from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from app import app

PASSWORD_VALIDATORS = (
    [
        DataRequired(),
        Length(4, 25),
        EqualTo("confirm", message="Les mots de passe encodés ne correspondent pas"),
    ]
    if app.debug
    else [
        DataRequired(),
        Length(12, 80),
        Regexp(
            r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!?(){}*$&@+=])",
            message="Le mot de passe doit contenir au moins une lettre minuscule, une majuscule, un chiffre et un caractère spécial : !?(){}*$&@+=",
        ),
    ]
)


class UserRegisterForm(FlaskForm):
    name = StringField(
        "Nom d'utilisateur", validators=[DataRequired(), Length(min=2, max=50)]
    )
    email = EmailField(
        "Email",
        validators=[
            DataRequired(),
            Email("L'adresse email est requise pour l'inscription"),
        ],
    )
    password = PasswordField("Mot de passe", validators=PASSWORD_VALIDATORS)
    confirm = PasswordField("Confirmation du mot de passe")
    firstname = StringField(
        "Prénom", validators=[DataRequired(), Length(min=2, max=50)]
    )
    lastname = StringField("Nom de famille", validators=[DataRequired(), Length(min=2, max=50)])
