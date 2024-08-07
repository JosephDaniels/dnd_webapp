from extensions import db
from models import Character
from webapp import app

with app.app_context():
    characters = Character.query.all()
    for char in characters:
        print(char.character_name, char.discord_username)