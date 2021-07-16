"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email

class AddPet(FlaskForm):
    
    name = StringField("Pet Name",
        validators=[InputRequired()])
    species = StringField("Species")
    photo_url = StringField("URL of pet's photo")
    age = SelectField("Age",
        choices=[('baby','Baby'), 
            ('young','Young'), 
            ('adult','Adult'), 
            ('senior', 'Senior')])
    notes = StringField("Notes")
    