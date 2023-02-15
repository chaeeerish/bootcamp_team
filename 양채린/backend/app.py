from flask import Flask
from db_connect import db
from flask_cors import CORS, cross_origin
from flask_jwt_extended import *
import logging

app = Flask(__name__)
# CORS(app, resources={r"*": {"origins": "http://localhost:8080"}})

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@127.0.0.1:3306/userdrawing"
app.config['SQLARCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ekdwls'

# 토큰 생성에 사용될 Secret Key를 flask 환경 변수에 등록
app.config.update(
			DEBUG = True,
			JWT_SECRET_KEY = "I'M IML"
		)

# JWT 확장 모듈을 flask 어플리케이션에 등록
jwt = JWTManager(app)

db.init_app(app)

# 블루프린트
from views import views
app.register_blueprint(views.bp)

if __name__ == '__main__':
    app.run(port=3000)
