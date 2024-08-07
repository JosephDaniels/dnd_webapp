# drop_temp_table.py
import sqlite3

connection = sqlite3.connect('characters.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS _alembic_tmp_character')
connection.commit()

connection.close()