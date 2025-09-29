from flask import Blueprint, render_template, redirect, url_for, request
from app.dao.referenciales.autores.autores_dto import AutoresDto
from app.dao.referenciales.autores.autores_dao import AutoresDao

autores_route = Blueprint('autores_route', __name__, template_folder='templates')
autores_dao = AutoresDao()
@autores_route.route('/')
def index():
    return render_template('autores-index.html', autores=autores_dao.leer())

#@autores_route.route('/editorial-form')
#def editorial_form():
 #   return render_template('editorial-form.html', combocursos=curso.leer())

@autores_route.route('/autores-form')
def autores_form():
    return render_template('autores-form.html')
    
@autores_route.route('/autores-alta', methods=['POST'])
def autores_alta():
    nombre_autor = request.form['nombre_autor']
 
    autores = AutoresDto(id=None, nombre_autor=nombre_autor)
    res = autores_dao.alta(autores)
    
    if res:
        return redirect(url_for('autores_route.index'))
    else:
        return redirect(url_for('autores_route.autores_form'))