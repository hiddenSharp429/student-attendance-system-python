"""
@coding : utf-8
@File   : app.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/6
@Desc   : Flask服务
@Version: version_1
@Last_editor jin Yang
"""

from flask import Flask
from flask_cors import CORS
from routes.student_routes import student_routes
from routes.teacher_routes import teacher_routes

app = Flask(__name__)
CORS(app)

# 注册蓝图
app.register_blueprint(student_routes)
app.register_blueprint(teacher_routes)

if __name__ == '__main__':
    print("Flask app is running on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000)

