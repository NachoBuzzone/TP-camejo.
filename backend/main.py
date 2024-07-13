from flask import Flask, request, jsonify
from models import db,Autos,Sucursales,Vendedores
from flask_cors import CORS

app = Flask(__name__)
CORS (app)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://santy23:Riverplate23@localhost:5432/concesionaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/autos', methods=['GET'])
def get_autos():
    try:
        autos = Autos.query.all()
        autos_data = []
        for auto in autos:
            auto_data = {
                'id': auto.id,
                'kilometraje': auto.kilometraje,
                'anio': auto.anio,
                'modelo': auto.modelo,
                'marca': auto.marca,
                'color': auto.color,
                'imagen': auto.imagen
            }
            autos_data.append (auto_data)
        return jsonify({'autos': autos_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route ('/autos/<id_autos>', methods = ["GET"])
def info_autos(id_autos):
    try:
        auto = Autos.query.get(id_autos)
        auto_data = {
            'id': auto.id,
            'kilometraje': auto.kilometraje,
            'anio': auto.anio,
            'modelo': auto.modelo,
            'marca': auto.marca,
            'color': auto.color,
            'imagen': auto.imagen
        }
        return jsonify (auto_data)
    except:
        return jsonify ({"mensaje: El auto no existe."})


@app.route('/autos', methods=['POST'])
def anadir_auto():
    try:
        data = request.json
        id = data.get ('id')
        kilometraje = data.get ('kilometraje')
        anio = data.get ('anio')
        modelo = data.get('modelo')
        marca = data.get('marca')
        color = data.get ('color')
        imagen = data.get ('imagen')
        auto_nuevo = Autos(id = id, kilometraje=kilometraje,anio=anio,modelo=modelo,marca=marca,color=color, imagen=imagen)
        db.session.add(auto_nuevo)
        db.session.commit()
        return jsonify({
            'Autos': {
                'id': auto_nuevo.id,
                'kilometraje': auto_nuevo.kilometraje,
                'anio': auto_nuevo.anio,
                'modelo': auto_nuevo.modelo,
                'marca': auto_nuevo.marca,
                'color': auto_nuevo.color,
                'imagen': auto_nuevo.imagen
            }
        }), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500


@app.route ('/autos/<id_autos>', methods = ["DELETE"])
def eliminar_auto (id_autos):
    auto = Autos.query.get (id_autos)
    db.session.delete (auto)
    db.session.commit ()
    return 


@app.route('/sucursales', methods=['POST'])
def anadir_sucursal():
    try:
        data = request.json
        id = data.get ('id')
        localidad = data.get ('localidad')
        direccion = data.get ('direccion')
        horario_de_atencion = data.get('horario_de_atencion')
        link_direccion = data.get ('link_direccion')
        sucursal_nueva = Sucursales(id = id, localidad=localidad,direccion=direccion,horario_de_atencion=horario_de_atencion, link_direccion=link_direccion)
        db.session.add(sucursal_nueva)
        db.session.commit()
        return jsonify({
            'Sucursales': {
                'id': sucursal_nueva.id,
                'localidad': sucursal_nueva.localidad,
                'direccion': sucursal_nueva.direccion,
                'horario_de_atencion': sucursal_nueva.horario_de_atencion,
                'link_direccion': sucursal_nueva.link_direccion
            }
        }), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500



@app.route('/sucursales', methods=['GET'])
def get_sucursales():
    try:
        sucursales= Sucursales.query.all()
        sucursales_data = []
        for sucursal in sucursales:
            sucursal_data = {
                'id': sucursal.id,
                'localidad': sucursal.localidad,
                'direccion': sucursal.direccion,
                'horario_de_atencion': sucursal.horario_de_atencion,
                'link_direccion': sucursal.link_direccion 
            }
            print (sucursal_data)
            sucursales_data.append(sucursal_data)
        return jsonify({'sucursales': sucursales_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500


@app.route ('/sucursales/<id_sucursales>', methods = ["GET"])
def info_sucursales(id_sucursales):
    try:
        sucursal = Sucursales.query.get(id_sucursales)
        sucursal_data = {
            'id': sucursal.id,
            'localidad': sucursal.localidad,
            'direccion': sucursal.direccion,
            'horario_de_atencion': sucursal.horario_de_atencion,
            'link_direccion': sucursal.link_direccion 
        }
        return jsonify (sucursal_data)
    except:
        return jsonify ({"mensaje: La sucursal no existe."})

        
@app.route('/vendedores', methods=['GET'])
def get_vendedores():
    try:
        vendedores = Vendedores.query.all()
        vendedores_data = []
        for vendedor in vendedores:
            vendedor_data = {
                'id': vendedor.id,
                'nombre': vendedor.nombre,
                'apellido': vendedor.apellido,
                'edad': vendedor.edad,
                'id_sucursal': vendedor.id_sucursal,
                'mail': vendedor.mail,
                'link_imagen': vendedor.link_imagen
            }
            vendedores_data.append (vendedor_data)
        return jsonify({'vendedores': vendedores_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route ('/vendedores/<id_vendedores>', methods = ["GET"])
def info_vendedores(id_vendedores):
    try:
        vendedor = Vendedores.query.get(id_vendedores)
        vendedor_data = {
            'id': vendedor.id,
            'nombre': vendedor.nombre,
            'apellido': vendedor.apellido,
            'edad': vendedor.edad,
            'id_sucursal': vendedor.id_sucursal,
            'mail': vendedor.mail,
            'link_imagen': vendedor.link_imagen
        }
        return jsonify (vendedor_data)
    except:
        return jsonify ({"mensaje: El vendedor no existe."})

@app.route('/vendedores', methods=['POST'])
def anadir_vendedor():
    try:
        data = request.json
        id = data.get ('id')
        nombre = data.get ('nombre')
        apellido = data.get ('apellido')
        edad = data.get ('edad')
        id_sucursal = data.get ('id_sucursal')
        mail = data.get('mail')
        link_imagen = data.get ('link_imagen')
        vendedor_nuevo = Vendedores(id = id, nombre=nombre,apellido=apellido,edad=edad,id_sucursal=id_sucursal,mail=mail, link_imagen=link_imagen)
        db.session.add(vendedor_nuevo)
        db.session.commit()
        return jsonify({
            'Vendedores': {
                'id': vendedor_nuevo.id,
                'nombre': vendedor_nuevo.nombre,
                'apellido': vendedor_nuevo.apellido,
                'edad': vendedor_nuevo.edad,
                'id_sucursal': vendedor_nuevo.id_sucursal,
                'mail': vendedor_nuevo.mail,
                'link_imagen': vendedor_nuevo.link_imagen
            }
        }), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route ('/vendedores/<id_vendedores>', methods = ["DELETE"])
def eliminar_sucursal (id_vendedores):
    vendedor = Vendedores.query.get (id_vendedores)
    db.session.delete (vendedor)
    db.session.commit ()
    return 

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)