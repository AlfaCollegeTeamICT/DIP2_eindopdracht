from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os
#Vergeet niet een nieuwe requirements file te maken als je nieuwe dingen toevoegd via pip install!

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'videotheek.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# !! Maak een class voor de gebruikers aan zodat er geregistreert en ingelogt kan worden zodat er een tabel beschikbaar is in de database
# Zorg ervoor dat deze gekoppeld word aan de logging tabel om ook te laten zien welke gebruiker een actie uitvoert

class Logging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)
    action = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default = datetime.now())
    

with app.app_context():
    db.create_all()

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

#voeg een route toe waar je bij komt op moment dat je naar een url gaat waar je geen toegang tot hebt.
#bijvoorbeeld op moment dat je naar de videotheek wil als je niet ingelogd bent

if __name__ == '__main__':
    app.run(debug=True)