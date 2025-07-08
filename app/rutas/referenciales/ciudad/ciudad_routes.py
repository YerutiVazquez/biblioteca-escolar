from flask import Blueprint, render_template

ciudad_route = Blueprint('ciudad_route', __name__, template_folder='templates')

@ciudad_route.route('/')
def index():
    return render_template('ciudad-index.html')