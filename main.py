from flask import Flask, request, jsonify
from models import db,Autos

app = Flask(__name__)
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
                'color': auto.color,
                'imagen': auto.imagen
            }
            autos_data.append (auto_data)
        return jsonify({'autos': autos_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)