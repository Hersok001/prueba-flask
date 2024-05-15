from random import sample
from flask import Blueprint, jsonify, request

from model.usuarioModel import User


usuarioController = Blueprint('usuarioController', __name__)

@usuarioController.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Se requiere nombre de usuario y contraseña'}), 400
    user = User.authenticate(username, password)
    if user:
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'message': 'Nombre de usuario o contraseña incorrectos'}), 401
    


