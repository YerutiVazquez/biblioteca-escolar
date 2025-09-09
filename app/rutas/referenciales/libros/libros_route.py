from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.dao.referenciales.libros.libros_dao import LibrosDto, LibrosDao # importar el modelo y dao para bd

libros_route = Blueprint('libros_route', __name__, template_folder='templates')
libros_dao = LibrosDao() # instancia del dao

@libros_route.route('/') # ruta del index /
def index():
    # render dibuja el html
    return render_template('libros-index.html', libros=libros_dao.leer())

@libros_route.route('/libros-form')
def libros_form():
    return render_template('libros-form.html')

@libros_route.route('/libros-form', methods=['POST'])
def libros_guardar():

    # datos que vienen del navegador

    titulo = request.form['Titulo']
    autores = request.form['Autores']
    ISBN = request.form['ISBN']
    año_publicacion = request.form['año_publicacion']
    genero = request.form['genero']
    cantidad_disponible = request.form['cantidad_disponible']
    ubicacion = request.form['ubicacion']
    id_editoriales = request.form['Editorial']
    
    # hacemos un objetito churro para el dao
    libro = LibrosDto(id=None, titulo=titulo, autores=autores, ISBN=ISBN, año_publicacion=año_publicacion, genero=genero, cantidad_disponible=cantidad_disponible, ubicacion=ubicacion, id_editoriales=id_editoriales)

    # el dao
    res = libros_dao.alta(libro)

    # en res viene true o falso
    # si vino false es que algo mambeo
    if res:
        # redirect necesita de la url de la vista
        # url for construye la url
        # se comen asi bien sabroso
        # render template no entra aca
        flash("Proceso exitoso", 'success')
        return redirect(url_for('libros_route.index'))
    else:
        flash("Ocurrio un error al procesar", 'danger')
        return redirect(url_for('libros_route.libros_form'))