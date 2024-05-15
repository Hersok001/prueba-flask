from flask import Blueprint, jsonify, request
from conexionBD import connect_mongodb
from bson.json_util import dumps

sensoresController = Blueprint('sensorController', __name__)

# Obtener los datos de todos los sensores
@sensoresController.route('/findAll', methods=['GET'])
def get_sensors():
    db = connect_mongodb()
    sensors = db['sensors'].find()
    print(sensors)
    sensors_list = list(sensors)  # Convertir a lista
    return dumps(sensors_list), 200

# Agregar datos de un sensor
@sensoresController.route('/create', methods=['POST'])
def add_sensor_data():
    data = request.get_json()
    db = connect_mongodb()
    result = db['sensors'].insert_one(data)
    if result:
        return jsonify({'message': 'Datos del sensor agregados correctamente'}), 200
    else:
        return jsonify({'message': 'Error al agregar datos del sensor'}), 500