from flask import Flask, render_template, request, redirect, url_for, flash, session
from extensions import db, migrate
from forms import CharacterForm
from models import Character

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AS(*$)OCS()$)DKL:S$Dkkd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///characters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def home():
    characters = Character.query.all()
    return render_template('index.html', characters=characters)

@app.route('/new', methods=['GET', 'POST'])
def new_character():
    form = CharacterForm()
    if form.validate_on_submit():
        new_char = Character(
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
            xp_points=form.xp_points.data,
        )
        db.session.add(new_char)
        db.session.commit()
        flash('Character created successfully!', 'success')
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            flash('Error creating character.', 'danger')

    return render_template('new_character.html', form=form)

@app.route('/edit/<int:char_id>', methods=['GET', 'POST'])
def edit_character(char_id):
    character = Character.query.get_or_404(char_id)
    form = CharacterForm(obj=character)
    if form.validate_on_submit():
        character.character_name = form.character_name.data
        character.discord_username = form.discord_username.data
        character.character_class = form.character_class.data
        character.alignment = form.alignment.data
        character.race = form.race.data
        character.age = form.age.data
        character.height = form.height.data
        character.weight = form.weight.data
        character.gender = form.gender.data
        character.eye_color = form.eye_color.data
        character.hair_color = form.hair_color.data
        character.skin_color = form.skin_color.data
        character.favorite_weapon = form.favorite_weapon.data
        character.character_description = form.character_description.data
        character.history = form.history.data
        character.strength = form.strength.data
        character.dexterity = form.dexterity.data
        character.constitution = form.constitution.data
        character.intelligence = form.intelligence.data
        character.wisdom = form.wisdom.data
        character.charisma = form.charisma.data
        character.maximum_health = form.maximum_health.data
        character.current_health = form.current_health.data
        character.xp_points = form.xp_points.data
        db.session.commit()
        flash('Character updated successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('edit_character.html', form=form, character=character)

if __name__ == "__main__":
    app.run(debug=True)
