from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class SiteForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired(), Length(min=2, max=255)])
    address = StringField('Adresse', validators=[DataRequired(), Length(min=2, max=255)])
    city = StringField('Ville', validators=[DataRequired(), Length(min=2, max=255)])