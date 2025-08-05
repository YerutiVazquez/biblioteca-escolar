from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.dao.referenciales.perso_adm.persoadm_dao import PersoadmDao
from app.dao.referenciales.perso_adm.persoadm_dto import PersoadmDto

# importar el modelo y dao para bd

persoadm_route = Blueprint('persoadm_route', __name__, template_folder='templates')
persoadm_dao = PersoadmDao() # instancia del dao

@persoadm_route.route('/') # ruta del index /
def index():
    # render dibuja el html
    return render_template('persoadm-index.html', persoadm=persoadm_dao.leer())

@persoadm_route.route('/persoadm-form')
def persoadm_form():
    return render_template('persoadm-form.html')

@persoadm_route.route('/persoadm-form', methods=['POST'])
def persoadm_guardar():
    
    # datos que vienen del navegador
    
    nombre = request.form['persoadm_nombre']
    apellido = request.form['persoadm_apellido']
    estado = request.form['persoadm_estado']
    cedula = request.form['persoadm_ci']  
    
    
    # hacemos un objetito churro para el dao
    persoadm = PersoadmDto(id=None, nombre=nombre, apellido=apellido,  estado=estado, ci=cedula,)
    
    # el dao
    res = persoadm_dao.alta(persoadm)   
    
    # en res viene true o falso
    # si vino false es que algo mambeo
    if res:
        # redirect necesita de la url de la vista
        # url for construye la url
        # se comen asi bien sabroso
        # render template no entra aca
        flash("Proceso exitoso", 'success')
        return redirect(url_for('persoadm_route.index'))
    else:
        flash("Ocurrio un error al procesar", 'danger')
        return redirect(url_for('persoadm_route.persoadm_form'))