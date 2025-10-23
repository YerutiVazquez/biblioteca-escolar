from flask import Flask

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q9z\n\xec]/'

from app.rutas.referenciales.institucion.institucion_routes import insti_route
from app.rutas.referenciales.inicio.inicio_routes import inicio_route
from app.rutas.referenciales.docentes.docente_route import docente_route
from app.rutas.referenciales.usuario.usuario_route import usuario_route
from app.rutas.referenciales.estudiantes.estu_route import estu_route

app.register_blueprint(inicio_route)

modulo0 = "/referenciales"
app.register_blueprint(insti_route, url_prefix=f'{modulo0}/institucion')
app.register_blueprint(docente_route, url_prefix=f'{modulo0}/docente')
app.register_blueprint(usuario_route, url_prefix=f'{modulo0}/usuario')
app.register_blueprint(estu_route, url_prefix=f'{modulo0}/estudiante')