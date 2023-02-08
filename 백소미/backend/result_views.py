# 결과 반환하는 페이지
# 프로세스 : 그림판 페이지에서 그림을 보내고 -> 모델에서 도출한 결과를 10.html로 결과 노출
# result_views => 결국 모델이 도출한 결과를 서버에 저장해 파라미터 값으로 10.html에 전송하는 역할?
# 전송된 값을 10.html을 통해 user에게 화면을 보여줌

#모델에서 값을 받아서 화면으로 보여주기
#데이터 정제 필요?
#모델에서 숫자와 텍스트로 값 준다고 했음

from flask import Blueprint, render_template, request, url_for, g, flash
import csv

bp = Blueprint('result_views', __name__, url_prefix='/result')

f = open('example.csv','r', encoding='utf8')
rdr = csv.DictReader(f)
str = 'hello, world'

@bp.route('/', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        for row in rdr:
            lst = dict(row)
        f.close()
        return render_template('10.html',\
                                datalist = lst, value = str)
    

