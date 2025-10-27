from flask import Blueprint, render_template, redirect, url_for, request
from app.dao.referenciales.estudiantes.estudiante_dao import EstudianteDao, EstudianteDto

estu_route = Blueprint('estu_route', __name__, template_folder='templates')
estu = EstudianteDao()

@estu_route.route('/')
def index():
    return render_template('estu-index.html', estu=estu.leer())

#@estu_route.route('/estudiante-form')
#def estudiante_form():
    #return render_template('estu-form.html', combocursos=curso.leer())

@estu_route.route('/estu-form', methods=['GET', 'POST'])
def estudiante_guardar():
    
    if request.method == 'GET':
        return render_template('estu-form.html')
    elif request.method == 'POST':
        cedula = request.form.get('estu_ci')
        nombres = request.form.get('estu_nombres')
        apellidos = request.form.get('estu_apellidos')
        telef = request.form.get('estu_telef')
        curso = request.form.get('estu_curso')
        turno = request.form.get('estu_turno')
        estudiante = EstudianteDto(id=None, nombres=nombres, apellidos=apellidos, ci=cedula, telef=telef,curso=curso, turno=turno)
        
        res = estu.alta(estudiante)
        
        if res:
            return redirect(url_for('estu_route.index'))
        else:
            return redirect(url_for('estu_route.estu-form'))
    
    