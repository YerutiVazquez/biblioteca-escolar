from flask import Blueprint, render_template, redirect, url_for, request
from app.dao.referenciales.editoriales.edioriales_dto import EditorialDto
from app.dao.referenciales.editoriales.editoriales_dao import EditorialDao

editorial_route = Blueprint('editorial_route', __name__, template_folder='templates')
editorial_dao = EditorialDao()
@editorial_route.route('/')
def index():
    return render_template('editorial-index.html', editorial=editorial_dao.leer())

#@editorial_route.route('/editorial-form')
#def editorial_form():
 #   return render_template('editorial-form.html', combocursos=curso.leer())

@editorial_route.route('/editorial-form')
def editorial_form():
    return render_template('editorial-form.html')
    
@editorial_route.route('/editorial-alta', methods=['POST'])
def editorial_alta():
    nombre_editorial = request.form['nombre_editorial']
    pais = request.form['pais_editorial']
 
    editorial = EditorialDto(id=None, nombres_editorial=nombre_editorial, pais=pais)
    res = editorial_dao.alta(editorial)
    
    if res:
        return redirect(url_for('editorial_route.index'))
    else:
        return redirect(url_for('editorial_route.editorial_form'))