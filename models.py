import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy ()

class Autos (db.Model):
    _tablename = 'autos'
    id = db.Column(db.Integer, primary_key=True)
    kilometraje = db.Column(db.Integer, nullable = False)
    anio = db.Column(db.Integer, nullable = False)
    modelo = db.Column(db.String(255), nullable = False)
    color = db.Column(db.String(50), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)