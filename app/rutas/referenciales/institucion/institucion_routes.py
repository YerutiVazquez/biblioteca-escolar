from flask import Blueprint, render_template

insti_route = Blueprint('insti_route', __name__, template_folder='templates')

@insti_route.route('/')
def index():
    return render_template('insti-index.html')