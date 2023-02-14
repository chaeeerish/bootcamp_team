from flask import Blueprint, render_template, request, url_for, g, flash, session, redirect, make_response, jsonify
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
    # test용
    # userid = '1'
    
    if userid is None:
        g.user = None
    else:
        g.user = db.session.query(User).filter(User.userid == userid).first()


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

@bp.route('/main/', methods=['POST', 'GET'])
def showMain():
    session.clear()
    if request.method == 'GET':
        return render_template('main.html')
    else: # POST
        '''
        request
            username

            ex) {"username": "yang"}
        '''
        # 세션 구현 해야함
        params = request.get_json()
        session['username'] = params['username']

        # insert
        user = User(username=params['username'])
        db.session.add(user)
        db.session.commit()

        session['userid'] = user.userid

        print(session['userid'])
        print(session['username'])

        return render_template('first.html')


@bp.route('/first/', methods=['POST', 'GET'])
def showFirst():
    if g.user == None:
        return redirect(url_for('views.showMain'))
    if request.method == 'POST':
        params = request.get_json()
        str = params['image']

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
        user = User.query.get_or_404(session['userid'])
        user.image1 = picture
        user.result1 = resultText
        db.session.commit()

        # 페이지 주기 => 페이지2
        return render_template("second.html")

@bp.route('/second/', methods=['POST', 'GET'])
def showSecond():
    if g.user == None:
        return redirect(url_for('views.showMain'))
    if request.method == 'POST':
        
        params = request.get_json()
        str = params['image']

        imgdata = base64.b64decode(str)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)

        picture = convertToBinaryData(filename) # 이미지를 binary로 변환하여 db에 저장하였다.

        # 모델 넣을 자리
        resultText = 'great!'

        # modify
        g.user.image2 = picture
        g.user.result2 = resultText
        db.session.commit()
        
        return render_template('third.html')


@bp.route('/third/', methods=['POST', 'GET'])
def showThird():
    if g.user == None:
        return redirect(url_for('views.showMain'))
    if request.method == 'GET':
        # response로 .. ?
        '''
        (make_response 함수 사용법)
        resp = make_response(render_template('error.html'), 404)
        resp.headers['X-Something'] = 'A value'
        return resp
        '''

        str_base641 = base64.b64encode(g.user.image1)
        base64_str1 = str_base641.decode('utf-8')

        str_base642 = base64.b64encode(g.user.image2)
        base64_str2 = str_base642.decode('utf-8')

        # version 1
        response = {
            "username": g.user.username,
            "image1": base64_str1,
            "image2": base64_str2,
            "result1": g.user.result1,
            "result2": g.user.result2
        }
        
        print(type(g.user))
        print(type(g.user.username))
        print(type(base64_str1))
        print(type(base64_str1))
        print(type(g.user.result1))
        print(type(g.user.result2))

        '''
        sitename_base64_str  = 'd2ViaXNmcmVl'
        sitename_bytes = base64.b64decode(sitename_base64_str )
        sitename = sitename_bytes .decode('ascii')
        '''    

        # version 1
        return jsonify({
            "username": g.user.username,
            "image1": base64_str1,
            "image2": base64_str2,
            "result1": g.user.result1,
            "result2": g.user.result2
        }), 200

        # version 2
        # return json.dumps(response)

        # 혹은 response에 담아서 보내는 방식도 있음.
        # redirect(location, statuscode, response)

@bp.route('/forth/', methods=['POST', 'GET'])
def showForth():
    if g.user == None:
        return redirect(url_for('views.showMain'))
    if request.method == 'GET':
        session.clear()       
        return render_template("forth.html")