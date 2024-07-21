from flask import Flask, request, jsonify, redirect, url_for, render_template
from models import db,Autos,Sucursales,Vendedores,Consultas,Login
from flask_cors import CORS
import random

app = Flask(__name__)
CORS (app)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://santy23:Riverplate23@localhost:5432/concesionaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

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
                'imagen': auto.imagen,
                'motor': auto.motor,
            }
            autos_data.append (auto_data)
            Autos.query.order_by(Autos.id).all()
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
            'imagen': auto.imagen,
            'motor': auto.motor,
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
        motor = data.get ('motor')
        auto_nuevo = Autos(id = id, kilometraje=kilometraje,anio=anio,modelo=modelo,marca=marca,color=color, imagen=imagen, motor=motor)
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
                'imagen': auto_nuevo.imagen,
                'motor': auto_nuevo.motor
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
    return ({'message' : 'Auto borrado exitosamente.'}), 200

@app.route ('/autos/<id_autos>', methods = ["PUT"])
def editar_auto(id_autos):
    try:
        data = request.json
        auto_editado = Autos.query.filter_by(id=id_autos).one()
        auto_editado.kilometraje = data.get('kilometraje')
        auto_editado.anio = data.get('anio')
        auto_editado.modelo = data.get('modelo')
        auto_editado.marca = data.get('marca')
        auto_editado.color = data.get('color')
        auto_editado.imagen = data.get('imagen')
        auto_editado.motor = data.get ('motor')

        db.session.commit()

        Autos.query.order_by(Autos.id).all ()
            
        actualizar_auto = {
            'id': auto_editado.id,
            'kilometraje': auto_editado.kilometraje,
            'anio': auto_editado.anio,
            'modelo': auto_editado.modelo,
            'marca': auto_editado.marca,
            'color': auto_editado.color,
            'imagen': auto_editado.imagen,
            'motor': auto_editado.motor
        }
            
        return jsonify({'Autos': actualizar_auto}), 200

    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500


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


@app.route ('/sucursales/<id_sucursales>', methods = ["PUT"])
def editar_sucursal(id_sucursales):
    try:
        data = request.json
        sucursal_editada = Sucursales.query.filter_by(id=id_sucursales).one()
        sucursal_editada.localidad = data.get('localidad')
        sucursal_editada.direccion = data.get('direccion')
        sucursal_editada.horario_de_atencion = data.get('horario_de_atencion')
        sucursal_editada.link_direccion = data.get('link_direccion')
            
        db.session.commit()
            
        actualizar_sucursal = {
            'id': sucursal_editada.id,
            'localidad': sucursal_editada.localidad,
            'direccion': sucursal_editada.direccion,
            'horario_de_atencion': sucursal_editada.horario_de_atencion,
            'link_direccion': sucursal_editada.link_direccion
        }
            
        return jsonify({'Sucursales': actualizar_sucursal}), 200

    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500


@app.route ('/sucursales/<id_sucursales>', methods = ["DELETE"])
def eliminar_sucursal(id_sucursales):
    sucursales = Sucursales.query.get (id_sucursales)
    vendedores = Vendedores.query.filter(Vendedores.id_sucursal == id_sucursales).all ()
    sucursales_restantes = Sucursales.query.filter(Sucursales.id!= id_sucursales).all ()
    for vendedor in vendedores:
        reasignar_sucursal = random.choice (sucursales_restantes)
        vendedor.id_sucursal = reasignar_sucursal.id
    db.session.commit ()
    db.session.delete (sucursales)
    db.session.commit ()
    return ({'message' : 'Sucursal borrada exitosamente.'}), 200

        
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

@app.route ('/vendedores/<id_vendedores>', methods = ["PUT"])
def editar_vendedor(id_vendedores):
    try:
        data = request.json
        vendedor_editado = Vendedores.query.filter_by(id=id_vendedores).one()
        vendedor_editado.nombre = data.get('nombre')
        vendedor_editado.apellido = data.get('apellido')
        vendedor_editado.edad = data.get('edad')
        vendedor_editado.id_sucursal = data.get('id_sucursal')
        vendedor_editado.mail = data.get('mail')
        vendedor_editado.link_imagen = data.get('link_imagen')
            
        db.session.commit()
            
        actualizar_vendedor = {
            'id': vendedor_editado.id,
            'nombre': vendedor_editado.nombre,
            'apellido': vendedor_editado.apellido,
            'edad': vendedor_editado.edad,
            'id_sucursal': vendedor_editado.id_sucursal,
            'mail': vendedor_editado.mail,
            'link_imagen': vendedor_editado.link_imagen
        }
            
        return jsonify({'Vendedores': actualizar_vendedor}), 200
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500


@app.route ('/vendedores/<id_vendedores>', methods = ["DELETE"])
def eliminar_vendedor (id_vendedores):
    vendedor = Vendedores.query.get (id_vendedores)
    db.session.delete (vendedor)
    db.session.commit ()
    return ({"message": "Vendedor borrado exitosamente"}),200


@app.route('/consultas', methods=['POST'])
def anadir_consulta():
    try:
        data = request.json
        id = data.get ('id')
        mail = data.get ('mail')
        tipo_consulta = data.get ('tipo_consulta')
        mensaje = data.get ('mensaje')
        consulta_nueva = Consultas(id = id, mail=mail,tipo_consulta=tipo_consulta,mensaje=mensaje)
        db.session.add(consulta_nueva)
        db.session.commit()
        return jsonify({
            'Consultas': {
                'id': consulta_nueva.id,
                'mail': consulta_nueva.mail,
                'tipo_consulta': consulta_nueva.tipo_consulta,
                'mensaje':consulta_nueva.mensaje
            }
        }), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500


@app.route('/consultas', methods=['GET'])
def get_info_consultas():
    try:
        consultas = Consultas.query.all()
        consultas_datos = []
        for consulta in consultas:
            info_consultas = {
                'id': consulta.id,
                'mail': consulta.mail,
                'tipo_consulta': consulta.tipo_consulta,
                'mensaje': consulta.mensaje
            }
            consultas_datos.append (info_consultas)
        return jsonify({'consultas': consultas_datos})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
 

@app.route('/login', methods=['POST'])
def iniciar_sesion():
    try:
        data = request.json
        id = data.get ('id')
        nombre = data.get ('nombre')
        apellido = data.get ('apellido')
        mail = data.get('mail')
        contrasena = data.get('contrasena')
        usuario = Login(id = id, nombre=nombre, apellido=apellido, mail=mail, contrasena=contrasena)
        db.session.add(usuario)
        db.session.commit()
        return jsonify({
            'Login': {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'apellido': usuario.apellido,
                'mail': usuario.mail,
                'contrasena': usuario.contrasena
            }
        }), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/login', methods=['GET'])
def get_info_login():
    try:
        informacion = Login.query.all()
        info_data = []
        for info in informacion:
            info_usuario_data = {
                'id': info.id,
                'nombre': info.nombre,
                'apellido': info.apellido,
                'mail': info.mail,
                'contrasena': info.contrasena
            }
            info_data.append (info_usuario_data)
        return jsonify({'informacion': info_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)