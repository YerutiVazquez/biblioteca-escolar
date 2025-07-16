from flask import Blueprint, render_template

estu_route = Blueprint('estu_route', __name__, template_folder='templates')

@estu_route.route('/')
def index():
    return render_template('estu-index.html')