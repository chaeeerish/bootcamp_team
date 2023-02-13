from flask import Blueprint, render_template, request, url_for, g, flash, session, redirect, make_response
import json
from db_connect import db
from werkzeug.utils import redirect
import base64
import sys
import uuid
# import tensorflow as tf

from models import User

bp = Blueprint('views', __name__, url_prefix='/')

'''
session
    userid
    username
'''

@bp.before_app_request
def load_sessioned_in_user():
    userid = session.get('userid')
    if userid is None:
        g.user = None
    else:
        g.user = db.session.query(User).filter(User.id == userid).first()


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

@bp.route('/main/')
def showMain():
    session.clear()
    if request.method == 'GET':
        return render_template('main.html')
    else: # POST
        # 세션 구현 해야함
        session['username'] = request.args['username']

        # insert
        user = User(username=request.args['username'])
        db.session.add(user)
        db.session.commit()

        session['userid'] = user.id

        print(session['userid'])
        print(session['username'])

        return render_template('first.html')


@bp.route('/first/', methods=['POST', 'GET'])
def showFirst():
    if request.method == 'POST':
        params = request.get_json()
        str = params['images']

        imgdata = base64.b64decode(str)
        filename = 'receivedimage.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)

        picture = convertToBinaryData(filename)      

        # 파이썬 파일 부르면서 매개변수로 넘겨주기
        # 학습 시킨 model 을 파일로 저장할 때, 보통 .h5 확장자로 저장합니다
        
        # 예시 코드1
        # model = tf.keras.models.load_model('model.h5') #모델 로드
        # resultText1 = model.predict(img) #예측값

        # 예시 코드2
        # 머신러닝 결과를 변수에 저장
        # predition = model.predict_food_transfer(model_transfer, test_transform, class_names, 'static/images/result.jpg')

        # 모델 넣을 자리
        resultText = 'great!'

        # modify
        user = User.query.get_or_404(session['id'])
        user.drawing1 = picture
        user.result1 = resultText
        db.session.commit()

        # 페이지 주기 => 페이지2
        return render_template("second.html")

@bp.route('/second/', methods=['POST', 'GET'])
def showSecond():
    if request.method == 'POST':
        
        params = request.get_json()
        str = params['images']

        imgdata = base64.b64decode(str)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)

        picture = convertToBinaryData(filename)

        # 모델 넣을 자리
        resultText = 'great!'

        # modify
        g.user.drawing2 = picture
        g.user.result2 = resultText
        db.session.commit()
        
        return render_template('third.html')


@bp.route('/third/', methods=['POST', 'GET'])
def showThird():
    if request.method == 'GET':
        # response로 .. ?
        '''
        (make_response 함수 사용법)
        resp = make_response(render_template('error.html'), 404)
        resp.headers['X-Something'] = 'A value'
        return resp
        '''
        '''
        <version 1>
        response = {
            "username": g.user.username,
            "image1": g.user.image1,
            "image2": g.user.image2,
            "result1": g.user.result1,
            "result2": g.user.result2
        }

        responseJson = json.dumps(response)
        # print(responseJson)
        session.clear()       
        
        return render_template('forth.html', var=responseJson)

        '''
        response = make_response(render_template('forth.html'))
        response.body

        # 혹은 response에 담아서 보내는 방식도 있음.

        # redirect(location, statuscode, response)
