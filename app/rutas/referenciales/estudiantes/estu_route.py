from flask import Blueprint, render_template, redirect, url_for, request
from app.dao.referenciales.estudiantes.estudiante_dao import EstudianteDao, EstudianteDto

estu_route = Blueprint('estu_route', __name__, template_folder='templates')
estu = EstudianteDao()

@estu_route.route('/')
def index():
    return render_template('estu-index.html', estu=estu.leer())

@estu_route.route('/estudiante-form')
def estudiante_form():
    return render_template('estu-form.html', combocursos=curso.leer())

@estu_route.route('/estudiante-form', methods=['POST'])
def estudiante_guardar():
    
    cedula = request.form['estu_ci']
    nombres = request.form['estu_nombres']
    apellidos = request.form['estu_apellidos']
    sexo = request.form['estu_sexo']
    estudiante = EstudianteDto(id=None, nombres=nombres, apellidos=apellidos, ci=cedula, sexo=sexo, curso=curso)
    
    res = estu.alta(estudiante)
    
    if res:
        return redirect(url_for('estu_route.index'))
    else:
        return redirect(url_for('estu_route.estudiante_form'))
    