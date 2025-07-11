from flask import Flask, jsonify, render_template, request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb #Importación del MySQL

app= Flask(__name__)

#Definir las variables
app.config['MYSQL_HOST']="localhost" #toma el 27001
app.config['MYSQL_USER']="root" #Definir el usuario
app.config['MYSQL_PASSWORD']="@SoyBienM0cha1" #Definir la pw
app.config['MYSQL_DB']="DBpeliculas"
app.secret_key= 'mysecretkey'
#app.config['MYSQL_PORT']="3306" //usar solo en cambio de puerto

#Declarar una variable de mysql pasando la estancia de MySQL de mi propia app
mysql= MySQL(app)

@app.route('/')
def home():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM Pelicula')
        consultaTodo= cursor.fetchall()
        return render_template('formulario.html', errores={}, albums= consultaTodo)
    
    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('formulario.html', errores={}, albums= [])
    finally:
        cursor.close()
        
@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM Pelicula WHERE id_pelicula=%s', (id,))
        consultaId= cursor.fetchone()
        return render_template('consulta.html', albums= consultaId)
    
    except Exception as e:
        print('Error al consultar por ID: '+e)
        return redirect(url_for('home'))
    
    finally:
        cursor.close()
        
@app.route('/actualizar/<int:id>')
def actualizar(id):
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM Pelicula WHERE id_pelicula=%s', (id,))
        consultaId= cursor.fetchone()
        return render_template('actualizar.html', album= consultaId, errores={})
    
    except Exception as e:
        print('Error al consultar por ID para actualizar: '+str(e))
        return redirect(url_for('home'))
    
    finally:
        cursor.close()
        
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado, Error de capa 8 !!!',404

@app.errorhandler(405)
def metodonoP(e):
    return 'Revisa el método del enío de tu ruta (GET o POST !!!)',405        

@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500
    


@app.route('/Guardarpelicula', methods=['POST'])
def guardar():
    
    errores={}
    
    Vtitulo= request.form.get('txtTitulo','').strip()
    Vdirector= request.form.get('txtDirector','').strip()
    Vanio= request.form.get('txtAnio','').strip()
    Vgenero= request.form.get('txtGenero','').strip()
    
    if not Vtitulo:
        errores['txtTitulo']= 'Nombre de la pelicula obligatorio'
    if not Vdirector:
        errores['txtDirector']= 'Nombre del director obligatorio'
    if not Vanio:
        errores['txtAnio']= 'Año es obligatorio'
    elif not Vanio.isdigit() or int(Vanio) < 1800 or int(Vanio) > 2100:
        errores['txtAnio']= 'Ingresa un año válido'
    if not Vgenero:
        errores['txtGenero']= 'Nombre del genero obligatorio'
        
    if not errores:
        try:
            cursor= mysql.connection.cursor()
            cursor.execute('insert into Pelicula(titulo, director, anio, genero) values(%s,%s,%s,%s)', (Vtitulo, Vdirector, Vanio, Vgenero)) #Inserciones de datos
            mysql.connection.commit()
            flash('La pelicula se guardo en BD')
            return redirect(url_for('home'))
        
        except Exception as e:
                mysql.connection.rollback()
                flash('Esta mal en algo, nimodotes pa'+ str(e))
                return redirect(url_for('home'))
            
        finally:
            cursor.close()
    
    return render_template('formulario.html', errores=errores)


if __name__ == '__main__':
    app.run(port=3000,debug=True)