from flask import Blueprint, render_template

inicio_route = Blueprint('inicio_route', __name__, template_folder='templates')

@inicio_route.route('/')
def index():
    return render_template('inicio-index.html')