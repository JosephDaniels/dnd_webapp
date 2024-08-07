from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import CharacterForm
from models import Character

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AS(*$)OCS()$)DKL:S$Dkkd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///characters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    characters = Character.query.all()
    return render_template('index.html', characters=characters)

@app.route('/new', methods=['GET', 'POST'])
def new_character():
    form = CharacterForm()
    if form.validate_on_submit():
        new_char = Character(
            name=form.name.data,
            race=form.race.data,
            char_class=form.char_class.data,
            level=form.level.data,
            strength=form.strength.data,
            dexterity=form.dexterity.data,
            constitution=form.constitution.data,
            intelligence=form.intelligence.data,
            wisdom=form.wisdom.data,
            charisma=form.charisma.data
        )
        db.session.add(new_char)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_character.html', form=form)

@app.route('/edit/<int:char_id>', methods=['GET', 'POST'])
def edit_character(char_id):
    character = Character.query.get_or_404(char_id)
    form = CharacterForm(obj=character)
    if form.validate_on_submit():
        character.name = form.name.data
        character.race = form.race.data
        character.char_class = form.char_class.data
        character.level = form.level.data
        character.strength = form.strength.data
        character.dexterity = form.dexterity.data
        character.constitution = form.constitution.data
        character.intelligence = form.intelligence.data
        character.wisdom = form.wisdom.data
        character.charisma = form.charisma.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_character.html', form=form, character=character)

if __name__ == "__main__":
    app.run(debug=True)