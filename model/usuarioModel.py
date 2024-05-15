
from conexionBD import connectionBD

class User:
    def __init__(self, id, username, password, activo, fcreacion):
        self.id = id
        self.username = username
        self.password = password
        self.activo = activo
        self.fcreacion = fcreacion

   
        
    @staticmethod
    def find_by_username(username):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)

        querySQL = "SELECT * FROM usuario WHERE usuario = %s"
        cur.execute(querySQL, (username,))
        user_data = cur.fetchone()

        cur.close()
        conexion_MySQLdb.close()

        if user_data:
            user_data['username'] = user_data.pop('usuario')
            return User(**user_data)
        else:
            return None    

    @staticmethod
    def authenticate(username, password):
        user = User.find_by_username(username)
        if user and user.password == password:
            return user
        else:
            return None

  