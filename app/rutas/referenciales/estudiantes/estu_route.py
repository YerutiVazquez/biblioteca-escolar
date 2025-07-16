from flask import Blueprint, render_template
from app.dao.referenciales.estudiantes.estudiante_dao import EstudianteDao

estu_route = Blueprint('estu_route', __name__, template_folder='templates')

@estu_route.route('/')
def index():
    estu = EstudianteDao()
    return render_template('estu-index.html', estu=estu.leer())