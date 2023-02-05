from flask import Blueprint, render_template, request, url_for, g, flash

bp = Blueprint('changing_views', __name__, url_prefix='/')

@bp.route('/', methods=['POST', 'GET'])
def show1():
    if request.method == 'GET':
        return render_template('1.html')

@bp.route('/2', methods=['POST', 'GET'])
def show2():
    if request.method == 'GET':
        return render_template('2.html')

@bp.route('/3', methods=['POST', 'GET'])
def show3():
    if request.method == 'GET':
        return render_template('3.html')

@bp.route('/4', methods=['POST', 'GET'])
def show4():
    if request.method == 'GET':
        return render_template('4.html')

## 5은 그림판

@bp.route('/6', methods=['POST', 'GET'])
def show6():
    if request.method == 'GET':
        return render_template('6.html')    


@bp.route('/7', methods=['POST', 'GET'])
def show7():
    if request.method == 'GET':
        return render_template('7.html')

## 8은 그림판

@bp.route('/9', methods=['POST', 'GET'])
def show9():
    if request.method == 'GET':
        return render_template('9.html')

## 10은 결과판
