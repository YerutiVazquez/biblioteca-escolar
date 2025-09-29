from flask import Blueprint, render_template, redirect, url_for, request, flash
from ....dao.referenciales.docentes.docente_dao import DocenteDao
from ....dao.referenciales.docentes.docente_dto import DocenteDto

docente_route = Blueprint('docente_route', __name__, template_folder='templates')
docente_dao = DocenteDao() # instancia del dao

@docente_route.route('/') # ruta del index /
def index():
    # render dibuja el html
    return render_template('docente-index.html', docente=docente_dao.leer())

@docente_route.route('/docente-form')
def docente_form():
    return render_template('docente-form.html')

@docente_route.route('/docente-form', methods=['POST'])
def docente_guardar():
    
    # datos que vienen del navegador
    
    nombre = request.form['docente_nombre']
    apellido = request.form['docente_apellido']
    ci= request.form['docente_ci']
    materia = request.form['docente_materia']  
    
    # hacemos un objetito churro para el dao
    docente = DocenteDto(id=None, nombre=nombre, apellido=apellido, ci=ci, materia=materia,)
    
    # el dao
    res = docente_dao.alta(docente)
    
    # en res viene true o falso
    # si vino false es que algo mambeo
    if res:
        # redirect necesita de la url de la vista
        # url for construye la url
        # se comen asi bien sabroso
        # render template no entra aca
        flash("Proceso exitoso", 'success')
        return redirect(url_for('docente_route.index'))
    else:
        flash("Ocurrio un error al procesar", 'danger')
        return redirect(url_for('docente_route.docente_form'))