import os
from flask import Flask, render_template, request, redirect, url_for
from extensions import db, migrate

app = Flask(__name__)

# Ensure the 'instance' directory exists for SQLite database
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'characters.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate
migrate.init_app(app, db)

# Import models after initializing db and migrate
from models import Character
from forms import CharacterForm

@app.route('/')
def home():
    characters = Character.query.all()
    return render_template('home.html', characters=characters)

@app.route('/new', methods=['GET', 'POST'])
def new_character():
    form = CharacterForm()
    if form.validate_on_submit():
        character = Character(
            character_name=form.character_name.data,
            discord_username=form.discord_username.data,
            character_class=form.character_class.data,
            alignment=form.alignment.data,
            race=form.race.data,
            age=form.age.data,
            height=form.height.data,
            weight=form.weight.data,
            gender=form.gender.data,
            eye_color=form.eye_color.data,
            hair_color=form.hair_color.data,
            skin_color=form.skin_color.data,
            favorite_weapon=form.favorite_weapon.data,
            character_description=form.character_description.data,
            history=form.history.data,
            strength=form.strength.data,
            dexterity=form.dexterity.data,
            constitution=form.constitution.data,
            intelligence=form.intelligence.data,
            wisdom=form.wisdom.data,
            charisma=form.charisma.data,
            maximum_health=form.maximum_health.data,
            current_health=form.current_health.data,
            armor_class=form.armor_class.data,
            xp_points=form.xp_points.data,
            platinum_coins=form.platinum_coins.data,
            gold_coins=form.gold_coins.data,
            silver_coins=form.silver_coins.data,
            copper_coins=form.copper_coins.data,
            feats=form.feats.data,
            special_abilities=form.special_abilities.data,
            skills=form.skills.data
        )
        db.session.add(character)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_character.html', form=form)

@app.route('/edit/<int:character_id>', methods=['GET', 'POST'])
def edit_character(character_id):
    character = Character.query.get_or_404(character_id)
    form = CharacterForm(obj=character)
    if form.validate_on_submit():
        form.populate_obj(character)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_character.html', form=form, character=character)

if __name__ == '__main__':
    app.run(debug=True)
