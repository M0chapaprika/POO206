from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb #Importación del MySQL

app= Flask(__name__)

#Definir las variables
app.config['MYSQL_HOST']="localhost" #toma el 27001
app.config['MYSQL_USER']="root" #Definir el usuario
app.config['MYSQL_PASSWORD']="SoyBienM0cha1" #Definir la pw
app.config['MYSQL_DB']="DBflask"
#app.config['MYSQL_PORT']="3306" //usar solo en cambio de puerto

#Declarar una variable de mysql pasando la estancia de MySQL de mi propia app
mysql= MySQL(app)

#ruta para probar la conexión a MySQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500

#Ruta simple
@app.route('/')
def home():
    return 'Hola Mundo FLASK'

#Ruta con parámetros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola, '+nombre+'!!!'

#Ruta try-catchs
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado, Error de capa 8 !!!',404

@app.errorhandler(405)
def metodonoP(e):
    return 'Revisa el método del envío de tu ruta (GET o POST !!!)',405

#Ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'soy el mismo recurso del servidor'

#Ruta POST
@app.route('/formulario',methods=['POST'])
def formulario():
    return 'soy un formulario :D'

if __name__ == '_main_':
    app.run(port=3000,debug=True)