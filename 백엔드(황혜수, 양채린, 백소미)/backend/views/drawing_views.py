from flask import Blueprint, render_template, request, url_for, g, flash

bp = Blueprint('drawing_views', __name__, url_prefix='/drawing')

@bp.route('/', methods=['POST', 'GET'])
def drawing():
    if request.method == 'GET':
        return render_template('index.html')
    else: # POST
        # 이미지 받기
        # 파이썬 파일 부르면서 매개변수로 넘겨주기
        # 파이썬 파일에서 csv 파일로 return 받기
        # 다음 페이지로 이동 => 페이지6
        pass
