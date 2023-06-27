#mi pagina web flask 
from flask import *
import pymongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_URL="mongodb://localhost:27017"
cliente = MongoClient(MONGO_URL)
db = cliente.flask
coleccion=db.videojuegos
coleecion2=db.materias
coleccion3=db.alimentos
coleccion4=db.quejas
app = Flask(__name__)


@app.route('/')#inicio
def pagina1():
    return render_template("pagina_principal.html")
@app.route('/2')#inicio de secion
def pagina2():
    return render_template("seccion_cuest.html")

#########################################################################################################################
@app.route('/3')#uestionario de videojuegos 
def pagina3():
    return render_template("cuestionario.html")

registros={}
numero_r=0
nombre = 0
marca= 0
donde =0
tiempo=0
fav=0
@app.route('/4',methods =['POST'])#envio de /3 
def pagina4():
    if request.method =='POST':
        global nombre, marca, donde, tiempo, fav, numero_r
        nombre= request.form['nombre']
        marca = request.form['marca']
        donde = request.form['donde']
        tiempo = request.form['tiempo']
        fav =request.form['fav']

        numero_r = +1
        id_encuesta = (str(numero_r))
        nueva_encuesta={
            "nombre" : nombre,
            "marca": marca,
            "donde": donde,
            "tiempo": tiempo,
            "fav": fav
        }
        registros.update({id_encuesta : nueva_encuesta})
        coleccion.insert_one(nueva_encuesta)
        print(nueva_encuesta)
        return redirect('http://localhost:5000/')
##############################################################################################################################
@app.route('/5')#sleccion de la graficacion de los datos 
def pagina5():
    return("esta es la 5 pagina algo mas que quieras???")  
###################################################################################################################################3
@app.route('/cien')
def cien():
    return render_template("cien.html")

@app.route('/arq')
def arq():
    return render_template("arq.html")

@app.route('/die')
def die():
    return render_template("die.html")

@app.route('/ele')
def ele():
    return render_template("ele.html")
@app.route('/cbti')
def cbti():
    return render_template("cbt.html")
@app.route('/metas')
def metas():
    return render_template("metas.html")
#######################################################################################################################################
@app.route('/quejas')
def quejas():
    return render_template('quejas.html')
nombre_q = 0
correo_q=0
queja=0
numero_q=0

@app.route('/subir_comentario',methods =['POST'])
def subir_comentario():
    if request.method =='POST':
        global nombre_q, correo_q, queja, numero_q
        nombre_q=request.form['nombre_q']
        correo_q=request.form['correo_q']
        queja= request.form['queja']

        numero_q=+1
        nueva_queja={
            "nombre_q" : nombre_q,
            "correo_q" : correo_q,
            "queja" : queja
        }
        coleccion4.insert_one(nueva_queja)
        return redirect('http://localhost:5000/')
##########################################################################################################################################
if __name__ == '__main__':
   app.run()