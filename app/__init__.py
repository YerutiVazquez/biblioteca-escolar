from flask import Flask

app = Flask(__name__)

from app.rutas.referenciales.ciudad.ciudad_routes import ciudad_route
from app.rutas.referenciales.institucion.institucion_routes import insti_route
from app.rutas.referenciales.inicio.inicio_routes import inicio_route
from app.rutas.referenciales.estudiantes.estu_route import estu_route
from app.rutas.referenciales.docentes.docente_route import docente_route

app.register_blueprint(inicio_route)

modulo0 = "/referenciales"
app.register_blueprint(ciudad_route, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(insti_route, url_prefix=f'{modulo0}/institucion')
app.register_blueprint(estu_route, url_prefix=f'{modulo0}/estudiante')
app.register_blueprint(docente_route, url_prefix=f'{modulo0}/docente')