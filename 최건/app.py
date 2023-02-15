from turtle import pd
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from flask import Flask, request
import json



app = Flask(__name__)
CORS(app, resources={r"/real_test": {"origins": "http://localhost:8080"}})

@app.route("/")
def helloWorld():
    return render_template('index.html')

@app.route("/real_test", methods=["GET","POST"])
@cross_origin(origin='http://localhost:8080')
def response_server():

    if request.method == 'POST':
        js_text = request.get_json()
        if 'userName' in js_text :
            text = js_text.get('userName')
        elif 'image1' in js_text :
            text = '이것은 이미지 1에 대한 리턴입니다.'
        elif 'image2' in js_text :
            text = '이것은 이미지 2에 대한 리턴입니다.'
        else :
            text = '오류'
        response = jsonify({'flask_text': 'flask에서 보냅니다','return':text})
    else :
        response = "1"
    return response

        # json_data = request.get_json()
        # vue_text = json_data.get('text')

        # flask_text = "flask에서 보냅니다."+vue_text
        # data = {'text': flask_text}
        # data.headers.add('Access-Control-Allow-Origin', '*')


if __name__=="__main__":
    app.run(debug=True)