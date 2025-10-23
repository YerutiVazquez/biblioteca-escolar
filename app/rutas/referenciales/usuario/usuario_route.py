from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.dao.referenciales.usuario.usuario_dao import UsuarioDao
from app.dao.referenciales.usuario.usuario_dto import UsuarioDto

# importar el modelo y dao para bd

usuario_route = Blueprint('usuario_route', __name__, template_folder='templates')
usuario_dao = UsuarioDao() # instancia del dao

@usuario_route.route('/') # ruta del index /
def index():
    # render dibuja el html 
    return render_template('usuario-index.html', usuario=usuario_dao.leer())

@usuario_route.route('/usuario-form/')
def usuario_form():
    return render_template('usuario-form.html')

@usuario_route.route('/usuario-form', methods=['POST'])
def usuario_guardar():
    
    # datos que vienen del navegador
    
    nombre = request.form['usuario_nombre']
    apellido = request.form['usuario_apellido']
    cedula = request.form['usuario_cedula']
    cargo = request.form['usuario_cargo']  
    usuario = request.form['usuario_usuario'] 
    passw = request.form['usuario_passw'] 
    
    
    # hacemos un objetito churro para el dao
    usuario = UsuarioDto(id_usuario=None, nombre=nombre, apellido=apellido,  cedula=cedula, cargo=cargo, usuario=usuario, passw=passw )
    
    # el dao
    res = usuario_dao.alta(usuario)   
    
    # en res viene true o falso
    # si vino false es que algo mambeo
    if res:
        # redirect necesita de la url de la vista
        # url for construye la url
        # se comen asi bien sabroso
        # render template no entra aca
        flash("Proceso exitoso", 'success')
        return redirect(url_for('usuario_route.index'))
    else:
        flash("Ocurrio un error al procesar", 'danger')
        return redirect(url_for('usuario_route.usuario_form'))