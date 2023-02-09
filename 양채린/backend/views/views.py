from flask import Blueprint, render_template, request, url_for, g, flash, session, redirect
from db_connect import db
from werkzeug.utils import redirect
import base64
import sys
# import tensorflow as tf

from models import User

bp = Blueprint('views', __name__, url_prefix='/main')

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

@bp.route('/')
def test():
    return render_template('index.html')


@bp.route('/1/', methods=['POST', 'GET'])
def showMainPage():
    if request.method == 'GET':
        return render_template('1.html')
    
    id = request.args['userid']
    name = request.args['username']

    str = request.data
    imgdata = base64.b64decode(str)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)

    print(type(str))

    picture = convertToBinaryData(filename)

    # 세션 구현 해야함
    session['id'] = request.args['userid']
    


    # 파이썬 파일 부르면서 매개변수로 넘겨주기
    # model = tf.keras.models.load_model('model.h5') #모델 로드
    # result = model.predict(img) #예측값

    user = User(userid=id, username=name, drawing1=picture)
    db.session.add(user)
    db.session.commit()

    # 페이지 주기 => 페이지2
    return render_template("2.html")

# @bp.route('/2/', methods=('GET', 'POST'))
# def drawing():
#     if request.method == 'POST':
#         if 'id' not in session:
#             return redirect(url_for('showMainPage'))
#         pass


# @bp.route('/3/', methods=('GET', 'POST'))
# def result():
#     if request.method == 'POST':
#         if 'id' not in session:
#             return redirect(url_for('showMainPage'))
#         # 2 완성되면
#         session.pop('id', None)
#         return render_template('3.html')