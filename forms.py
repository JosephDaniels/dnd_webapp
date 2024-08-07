from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    race = StringField('Race', validators=[DataRequired()])
    char_class = StringField('Class', validators=[DataRequired()])
    level = IntegerField('Level', validators=[DataRequired(), NumberRange(min=1, max=20)])
    strength = IntegerField('Strength', validators=[DataRequired(), NumberRange(min=1, max=20)])
    dexterity = IntegerField('Dexterity', validators=[DataRequired(), NumberRange(min=1, max=20)])
    constitution = IntegerField('Constitution', validators=[DataRequired(), NumberRange(min=1, max=20)])
    intelligence = IntegerField('Intelligence', validators=[DataRequired(), NumberRange(min=1, max=20)])
    wisdom = IntegerField('Wisdom', validators=[DataRequired(), NumberRange(min=1, max=20)])
    charisma = IntegerField('Charisma', validators=[DataRequired(), NumberRange(min=1, max=20)])
    submit = SubmitField('Create Character')