from flask import Flask
from db_connect import db
import logging
 
logging.basicConfig(filename = "logs/project.log", level = logging.DEBUG)
application=Flask(__name__)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@127.0.0.1:3306/userdrawing"
app.config['SQLARCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ekdwls'

db.init_app(app)

# 블루프린트
from views import views
app.register_blueprint(views.bp)

if __name__ == '__main__':
    app.run()
