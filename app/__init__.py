from flask import Flask

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q9z\n\xec]/'

from app.rutas.referenciales.ciudad.ciudad_routes import ciudad_route
from app.rutas.referenciales.institucion.institucion_routes import insti_route
from app.rutas.referenciales.inicio.inicio_routes import inicio_route
from app.rutas.referenciales.estudiantes.estu_route import estu_route
from app.rutas.referenciales.docentes.docente_route import docente_route
from app.rutas.referenciales.perso_adm.persoadm_route import persoadm_route
from app.rutas.referenciales.editoriales.editorial_route import editorial_route

app.register_blueprint(inicio_route)

modulo0 = "/referenciales"
app.register_blueprint(ciudad_route, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(insti_route, url_prefix=f'{modulo0}/institucion')
app.register_blueprint(estu_route, url_prefix=f'{modulo0}/estudiante')
app.register_blueprint(docente_route, url_prefix=f'{modulo0}/docente')
app.register_blueprint(persoadm_route, url_prefix=f'{modulo0}/persoadm')
app.register_blueprint(editorial_route, url_prefix=f'{modulo0}/editoriales')
                       