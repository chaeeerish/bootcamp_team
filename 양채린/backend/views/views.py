from flask import Blueprint, render_template, request, url_for, g, flash, session, redirect
from db_connect import db
from werkzeug.utils import redirect
import base64
import sys
import uuid
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
    # 학습 시킨 model 을 파일로 저장할 때, 보통 .h5 확장자로 저장합니다
    
    # 예시 코드1
    # model = tf.keras.models.load_model('model.h5') #모델 로드
    # resultText1 = model.predict(img) #예측값

    # 예시 코드2
    # 머신러닝 결과를 변수에 저장
    # predition = model.predict_food_transfer(model_transfer, test_transform, class_names, 'static/images/result.jpg')
    resultText = ''

    # insert
    user = User(userid=id, username=name, drawing1=picture, result1=resultText)
    db.session.add(user)
    db.session.commit()

    # 페이지 주기 => 페이지2
    return render_template("2.html")

@bp.route('/2/', methods=['POST', 'GET'])
def drawing():
    if request.method == 'POST':
        if session['id'] != request.args['id']:
            return redirect(url_for('views.showMainPage'))
        str = request.data
        imgdata = base64.b64decode(str)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)

        picture = convertToBinaryData(filename)

        # 모델 넣을 자리
        resultText = ''

        # modify
        user = User.query.get_or_404(session['id'])
        user.drawing2 = picture
        user.result2 = resultText
        db.session.commit()
        
        return redirect(url_for('views.result'))


@bp.route('/3/', methods='GET')
def result():
    if request.method == 'GET':
        if session['id'] != request.args['id']:
            return redirect(url_for('views.showMainPage'))
        
        user = User.query.get_or_404(session['id'])
        result1 = user.result1
        result2 = user.result2

        session.pop('id', None)
        # 이 방식은 template에 넣어주는 형식
        return render_template('4.html', result1=result1, result2=result2)
        # 혹은 response에 담아서 보내는 방식도 있음.

        # redirect(location, statuscode, response)
