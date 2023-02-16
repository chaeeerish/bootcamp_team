from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import request
from flask import render_template, redirect, url_for, request
from flask import jsonify

from tensorflow import keras
from keras.models import Sequential

import io
from PIL import Image
import cv2


import numpy as np
import pickle as p
import json

app = Flask(__name__)
api = Api(app)


class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args=parser.parse_args()

            _userEmail = args['email']
            _userName = args['user_name']
            _userPassword = args['password']

            return {'Email': args['email'], 
                    'UserName': args['user_name'],
                    'Password': args['password']}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/user')
@app.route("/exam")

def get_model():
    # # Create a simple model.
    # inputs = keras.Input(shape=(32,))
    # outputs = keras.layers.Dense(1)(inputs)
    # model = keras.Model(inputs, outputs)
    # model.compile(optimizer="adam", loss="mean_squared_error")
    model = keras.models.load_model('save_model.h5')
    # model.summary()
    return model
model = get_model()


# def predict():


@app.route('/')
def home():
    image = cv2.imread('./image/test_1.PNG')
    # return 'This is home!'

# @app.route('/predict/', methods=['POST'])
# def predict():
#     parser = reqparse.RequestParser()
#     parser.add_argment('petal_length')
#     parser.add_argument('petal_width')
#     parser.add_argument('separ_length')
#     parser.add_argument('sepal_width')

#     #create dict, 위의 내용을 딕셔너리로 저장한다.
#     args = parser.parse_args()
#     print(args)

#     #convert input to array
#     X_new = np.fromiter(args.values(), dtype=float)
#     print(X_new)

#     #predict - return ndarrya
#     prediction = model.predict([X_new])

#     #result
#     out = {'Prediction': get_label(prediction[0])}

#     return out, 200

# def get_label(label_num):
#     labels={'0':'iris-setosa',
#             '1':'iris-versicolor',
#             '2':'iris-virginica'}
#     return labels.get(str(label_num))



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
