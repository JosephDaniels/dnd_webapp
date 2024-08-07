from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CharacterForm(FlaskForm):
    character_name = StringField('Character Name', validators=[DataRequired()])
    discord_username = StringField('Discord Username', validators=[DataRequired()])
    character_class = SelectField('Class', choices=[
        ('Fighter', 'Fighter'), ('Wizard', 'Wizard'), ('Bard', 'Bard'), ('Monk', 'Monk'),
        ('Paladin', 'Paladin'), ('Barbarian', 'Barbarian'), ('Sorcerer', 'Sorcerer'),
        ('Rogue', 'Rogue')
    ], validators=[DataRequired()])
    alignment = SelectField('Alignment', choices=[
        ('Lawful Good', 'Lawful Good'), ('Neutral Good', 'Neutral Good'), ('Chaotic Good', 'Chaotic Good'),
        ('Lawful Neutral', 'Lawful Neutral'), ('True Neutral', 'True Neutral'),
        ('Chaotic Neutral', 'Chaotic Neutral'), ('Lawful Evil', 'Lawful Evil'),
        ('Neutral Evil', 'Neutral Evil'), ('Chaotic Evil', 'Chaotic Evil')
    ], validators=[DataRequired()])
    race = SelectField('Race', choices=[
        ('Human', 'Human'), ('Elven', 'Elven'), ('Orcish', 'Orcish'),
        ('Dwarven', 'Dwarven'), ('Gnome', 'Gnome'), ('Tiefling', 'Tiefling'),
        ('Drow', 'Drow')
    ], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    height = StringField('Height', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[
        ('Male', 'Male'), ('Female', 'Female'), ('Non-Binary', 'Non-Binary'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    eye_color = StringField('Eye Color', validators=[DataRequired()])
    hair_color = StringField('Hair Color', validators=[DataRequired()])
    skin_color = StringField('Skin Color', validators=[DataRequired()])
    favorite_weapon = StringField('Favorite Weapon', validators=[DataRequired()])
    character_description = TextAreaField('Character Description', validators=[DataRequired()])
    history = TextAreaField('History', validators=[DataRequired()])
    strength = IntegerField('Strength', validators=[DataRequired(), NumberRange(min=1, max=20)])
    dexterity = IntegerField('Dexterity', validators=[DataRequired(), NumberRange(min=1, max=20)])
    constitution = IntegerField('Constitution', validators=[DataRequired(), NumberRange(min=1, max=20)])
    intelligence = IntegerField('Intelligence', validators=[DataRequired(), NumberRange(min=1, max=20)])
    wisdom = IntegerField('Wisdom', validators=[DataRequired(), NumberRange(min=1, max=20)])
    charisma = IntegerField('Charisma', validators=[DataRequired(), NumberRange(min=1, max=20)])
    maximum_health = IntegerField('Maximum Health', validators=[DataRequired()])
    current_health = IntegerField('Current Health', validators=[DataRequired()])
    xp_points = IntegerField('XP Points', validators=[DataRequired()])
    submit = SubmitField('Submit')
