"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import AnyOf, InputRequired, Optional, URL
from wtforms.widgets.core import Input

class AddPet(FlaskForm):
    """form to add a pet to our database"""

    age_choices = [
            ('baby','Baby'), 
            ('young','Young'), 
            ('adult','Adult'), 
            ('senior', 'Senior')]
    name = StringField("Pet Name", 
        validators=[InputRequired()])
    species = StringField(
        "Species", 
        validators=[
            AnyOf(values=['cat', 'dog', 'porcupine']),
            InputRequired()
            ])
    photo_url = StringField(
        "URL of pet's photo",
        validators=[URL(require_tld=True), Optional()]
        )
    age = SelectField(
        "Age",
        choices = age_choices,
        validators=[
            AnyOf(values = ['baby', 'young', 'adult', 'senior']),
            InputRequired()
            ])
    notes = StringField("Notes", validators=[Optional()])
    
class PetEditForm(FlaskForm):
    """form to edit pet details"""
    
    photo_url = StringField(
        "URL of pet's photo",
        validators=[URL(require_tld=True),
        Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available to adopt")
