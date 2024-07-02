'''
Author: hiddenSharp429 z404878860@163.com
Date: 2024-07-02 11:50:19
LastEditors: hiddenSharp429 z404878860@163.com
LastEditTime: 2024-07-02 11:53:36
FilePath: /Student Attendance System/test/test_student_routes.py
Description: 学生端路由测试
'''
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from routes.student_routes import view_all_students, view_student_courses, verify_stu_login, view_signal_student, punch_in, absence_on_leave, search_student_course

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

def test_view_all_students(app):
    with app.test_request_context(headers={'app': 'wx-app'}):
        response = view_all_students()
        print(response)

def test_view_student_courses(app):
    test_student_id = '2021611001'
    test_semester = '2023'
    test_week_no = 5
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app'},
                                  query_string={'student_id': test_student_id, 'semester': test_semester, 'week_no': test_week_no}):
        response = view_student_courses()
        print(response)

def test_verify_stu_login(app):
    test_student_id_login = '2021611007'
    test_student_name_login = '祝子贤'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app'},
                                  query_string={'student_id': test_student_id_login, 'student_name': test_student_name_login}):
        response = verify_stu_login()
        print(response)

def test_view_signal_student(app):
    test_student_id = '2021611001'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app'},
                                  query_string={'student_id': test_student_id}):
        response = view_signal_student()
        print(response)

def test_punch_in(app):
    test_student_id = '2021611011'
    test_punch_in_time = '2024-01-03 09:20:34'
    test_code = 'c0003'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'},
                                  data={'student_id': test_student_id, 'punch_in_time': test_punch_in_time, 'code': test_code}):
        response = punch_in()
        print(response)

def test_absence_on_leave(app):
    test_student_id_leave = '2021611011'
    test_course_id_leave = 'c1'
    test_teacher_id_leave = 'T001'
    test_course_number_leave = 17
    test_reason = '生病请假'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'},
                                  data={'student_id': test_student_id_leave, 'course_id': test_course_id_leave, 'teacher_id': test_teacher_id_leave, 'course_number': test_course_number_leave, 'reason': test_reason}):
        response = absence_on_leave()
        print(response)

def test_search_student_course(app):
    test_student_id = '2021611003'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app'},
                                  query_string={'student_id': test_student_id}):
        response = search_student_course()
        print(response)
        print(response[0].json)