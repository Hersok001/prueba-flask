from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller.usuarioController import *
from controller.sensoresController import *
from flask_cors import CORS


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
CORS(app)
application = app

@app.route('/')
def index():
    return '¡Hola, mundo!'


app.register_blueprint(usuarioController, url_prefix='/auth')
app.register_blueprint(sensoresController, url_prefix='/sensors')

#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)