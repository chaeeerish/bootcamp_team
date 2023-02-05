from flask import Flask

app = Flask(__name__)

# 블루프린트
from views import drawing_views, changing_views, result_views
app.register_blueprint(drawing_views.bp)
app.register_blueprint(changing_views.bp)
app.register_blueprint(result_views.bp)

if __name__ == '__main__':
    app.run()
