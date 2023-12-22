"""
@coding : utf-8
@File   : __init__.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/17
@Desc   : 
@Version:
@Last_editor
"""
from flask import Blueprint

student_routes = Blueprint('student_routes', __name__)
teacher_routes = Blueprint('teacher_routes', __name__)


# Import route handlers
from . import student_routes
from . import teacher_routes

if __name__ == "__main__":
    pass
