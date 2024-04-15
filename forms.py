""" Forms for app """

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange


class AddPetForm(FlaskForm):
    """ Form for adding a new pet """

    name = StringField("Pet's name: ",
                       validators=[InputRequired()])
    species = SelectField('Species of pet:',
                          choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')], 
                          validators=[InputRequired()])
    photo_url = StringField('Link to photo of pet')
    age = IntegerField("Age of pet (years):",
                       validators=[NumberRange(min=0, max=30)])
    notes = StringField('Enter any additional notes about the pet:')

class EditPetForm(FlaskForm):
    """ Form to edit pet's details """
    
    photo_url = StringField('Link to photo of pet')
    notes = StringField('Enter any additional notes about the pet')
    available = BooleanField('Available for adoption?')
    