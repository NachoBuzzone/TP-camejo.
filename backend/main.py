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
                'en_actividad': sucursal.en_actividad,
                'link_direccion': sucursal.link_direccion 
            }
            print (sucursal_data)
            sucursales_data.append(sucursal_data)
        return jsonify({'sucursales': sucursales_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
