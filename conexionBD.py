import mysql.connector
from pymongo import MongoClient

def connectionBD():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="root",
        database = "prueba_flask"
        )
    if mydb:
        return mydb
    else:
        print("Error en la conexion a BD")
        
def connect_mongodb():
    try:     
        uri = "mongodb+srv://root:root@pruebaflask.hoseyrb.mongodb.net/sample_mflix?retryWrites=true&w=majority&appName=pruebaFlask"       
        client = MongoClient(uri)       
        db = client.sample_mflix
        client.server_info()  
        
        return db
    except Exception as e:
        print('Error al conectarse a MongoDB:', e)
        return None