# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

class CharacterForm(FlaskForm):
    character_name = StringField('Character Name', validators=[DataRequired()])
    discord_username = StringField('Discord Username', validators=[DataRequired()])

    character_class = SelectField('Class', choices=[
        ('barbarian', 'Barbarian'),
        ('bard', 'Bard'),
        ('cleric', 'Cleric'),
        ('druid', 'Druid'),
        ('fighter', 'Fighter'),
        ('monk', 'Monk'),
        ('paladin', 'Paladin'),
        ('ranger', 'Ranger'),
        ('rogue', 'Rogue'),
        ('sorcerer', 'Sorcerer'),
        ('wizard', 'Wizard')
    ], validators=[DataRequired()])

    alignment = SelectField('Alignment', choices=[
        ('lg', 'Lawful Good'),
        ('ng', 'Neutral Good'),
        ('cg', 'Chaotic Good'),
        ('ln', 'Lawful Neutral'),
        ('tn', 'True Neutral'),
        ('cn', 'Chaotic Neutral'),
        ('le', 'Lawful Evil'),
        ('ne', 'Neutral Evil'),
        ('ce', 'Chaotic Evil')
    ], validators=[DataRequired()])

    race = SelectField('Race', choices=[
        ('human', 'Human'),
        ('elf', 'Elf'),
        ('dwarf', 'Dwarf'),
        ('halfling', 'Halfling'),
        ('gnome', 'Gnome'),
        ('half_elf', 'Half-Elf'),
        ('half_orc', 'Half-Orc'),
        ('tiefling', 'Tiefling'),
        ('dragonborn', 'Dragonborn')
        # Add more races here
    ], validators=[DataRequired()])

    age = IntegerField('Age', validators=[DataRequired()])
    height = StringField('Height', validators=[DataRequired()])
    weight = StringField('Weight', validators=[DataRequired()])

    gender = SelectField('Gender', choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-Binary'),
        ('other', 'Other')
    ], validators=[DataRequired()])

    eye_color = StringField('Eye Color', validators=[DataRequired()])
    hair_color = StringField('Hair Color', validators=[DataRequired()])
    skin_color = StringField('Skin Color', validators=[DataRequired()])
    favorite_weapon = StringField('Favorite Weapon', validators=[DataRequired()])
    character_description = TextAreaField('Description', validators=[DataRequired()])
    history = TextAreaField('History', validators=[DataRequired()])

    strength = IntegerField('Strength', validators=[DataRequired()])
    dexterity = IntegerField('Dexterity', validators=[DataRequired()])
    constitution = IntegerField('Constitution', validators=[DataRequired()])
    intelligence = IntegerField('Intelligence', validators=[DataRequired()])
    wisdom = IntegerField('Wisdom', validators=[DataRequired()])
    charisma = IntegerField('Charisma', validators=[DataRequired()])

    maximum_health = IntegerField('Maximum Health', validators=[DataRequired()])
    current_health = IntegerField('Current Health', validators=[DataRequired()])
    armor_class = IntegerField('Armor Class', validators=[DataRequired()])
    xp_points = IntegerField('XP Points', validators=[DataRequired()])

    platinum_coins = IntegerField('Platinum Coins', validators=[DataRequired()])
    gold_coins = IntegerField('Gold Coins', validators=[DataRequired()])
    silver_coins = IntegerField('Silver Coins', validators=[DataRequired()])
    copper_coins = IntegerField('Copper Coins', validators=[DataRequired()])

    feats = SelectMultipleField('Feats', choices=[
        ('power_attack', 'Power Attack'),
        ('dodge', 'Dodge'),
        ('weapon_focus', 'Weapon Focus')
        # Add more feats here
    ], validators=[DataRequired()])

    special_abilities = TextAreaField('Special Abilities')
    skills = TextAreaField('Skills')

    submit = SubmitField('Submit')
