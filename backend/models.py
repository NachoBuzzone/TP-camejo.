import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy ()

class Autos (db.Model):
    _tablename = 'autos'
    id = db.Column(db.Integer, primary_key=True)
    kilometraje = db.Column(db.Integer, nullable = False)
    anio = db.Column(db.Integer, nullable = False)
    modelo = db.Column(db.String(255), nullable = False)
    marca = db.Column (db.String (255), nullable = False)
    color = db.Column(db.String(50), nullable = False)
    imagen = db.Column(db.String(255), nullable = False)

class Sucursales(db.Model):
    _tablename = 'sucursales'
    id = db.Column(db.Integer, primary_key=True)
    localidad = db.Column(db.String(250),nullable = False)
    direccion = db.Column(db.String(250), nullable = False)
    horario_de_atencion = db.Column(db.String(255), nullable = False)
    link_direccion = db.Column(db.String(255), nullable = False)

class Vendedores (db.Model):
    _tablename = 'vendedores'
    id = db.Column (db.Integer, primary_key= True)
    nombre = db.Column (db.String (255), nullable = False)
    apellido = db.Column (db.String (255), nullable = False)
    edad = db.Column (db.Integer, nullable = False)
    id_sucursal = db.Column (db.Integer,db.ForeignKey('sucursales.id'))
    mail = db.Column (db.String (255),nullable = False)
    link_imagen = db.Column (db.String (255), nullable = False)
