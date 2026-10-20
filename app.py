from flask import Flask, render_template
from flask_cors import CORS
import sqlite3
import os

#Vergeet niet een nieuwe requirements file te maken als je nieuwe dingen toevoegd via pip install!
# $ pip freeze > requirements.txt

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.urandom(32)
DATABASE = os.path.join(basedir, 'videotheek.db')

CORS(app)

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

def create_database():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS film (
            id INTEGER PRIMARY KEY,
            title VARCHAR(150) NOT NULL,
            status VARCHAR(50) NOT NULL
        )
    ''')

    # !! Maak een tabel voor de gebruikers aan zodat er geregistreert en ingelogt kan worden
    # Zorg ervoor dat deze gekoppeld word aan de logging tabel om ook te laten zien welke gebruiker een actie uitvoert

    conn.execute('''
        CREATE TABLE IF NOT EXISTS logging (
            id INTEGER PRIMARY KEY,
            film_id INTEGER NOT NULL,
            action INTEGER NOT NULL,
            timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (film_id) REFERENCES film (id)
        )
    ''')
    conn.commit()
    conn.close()

# Aanmaken database
create_database()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/videotheek')
#Zorg ervoor dat deze route alleen werkt als je ingelogt bent
def videotheek():
    return render_template('videotheek.html')

@app.route('/login')
def login():
    #login afmaken
    return render_template('login.html')

@app.route('/register')
def register():
    #registreren afmaken
    return render_template('register.html')

@app.route('/logout')
def logout():
    #logout functionaliteit toevoegen de pass mag hiervoor weggehaald worden
    pass

@app.route('/opdracht')
def opdracht():
    return render_template('opdracht.html')

#voeg een route toe waar je bij komt op moment dat je naar een url gaat waar je geen toegang tot hebt.
#bijvoorbeeld op moment dat je naar de videotheek wil als je niet ingelogd bent

if __name__ == '__main__':
    app.run(debug=True)