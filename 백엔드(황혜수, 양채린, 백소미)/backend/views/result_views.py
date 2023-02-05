from flask import Blueprint, render_template, request, url_for, g, flash

bp = Blueprint('result_views', __name__, url_prefix='/result')

@bp.route('/', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        return render_template('10.html')
    
