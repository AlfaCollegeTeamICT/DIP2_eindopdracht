from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

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

# !! Maak een class voor de gebruikers aan zodat er geregistreert en ingelogt kan worden zodat er een tabel beschikbaar is in de database

class Logging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)
    renttimestamp = db.Column(db.DateTime, nullable=False, default = datetime.now())
    returntimestamp = db.Column(db.DateTime, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/videotheek')
def videotheek():
    return render_template('videotheek.html')

if __name__ == '__main__':
    app.run(debug=True)