'''
Author: hiddenSharp429 z404878860@163.com
Date: 2024-07-02 12:03:15
LastEditors: hiddenSharp429 z404878860@163.com
LastEditTime: 2024-07-02 12:07:22
FilePath: /Student Attendance System/test/test_teacher_routes.py
Description: 教师端路由测试
'''
import sys
import os
import pytest
from flask import Flask, json
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from routes.teacher_routes import verify_teacher_login, view_absentee_list, post_attendance, view_signal_teacher, get_leave_requests, search_teacher_course, review_leave_request

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

def test_verify_teacher_login(app):
    test_teacher_id_login = 'T001'
    test_teacher_name_login = '张老师'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app'},
                                  query_string={'teacher_id': test_teacher_id_login, 'teacher_name': test_teacher_name_login}):
        response = verify_teacher_login()
        print(response)

def test_view_absentee_list(app):
    test_course_id = 'c1'
    test_course_no = 2
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app'},
                                  query_string={'course_id': test_course_id, 'course_no': test_course_no}):
        response = view_absentee_list()
        print(response)

def test_post_attendance(app):
    one_day = timedelta(days=1)
    test_course_name = '操作系统原理'
    test_course_id = 'c1'
    test_course_no = 17
    test_attendance_start_time = datetime.now()
    test_attendance_end_time = datetime.now() + one_day
    test_code = 'c0002'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'},
                                  data={'course_name': test_course_name, 'course_id': test_course_id, 'course_no': test_course_no,
                                        'attendance_start_time': test_attendance_start_time, 'attendance_end_time': test_attendance_end_time,
                                        'code': test_code}):
        response = post_attendance()
        print(response)

def test_view_signal_teacher(app):
    test_teacher_id = 'T001'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app'},
                                  query_string={'teacher_id': test_teacher_id}):
        response = view_signal_teacher()
        print(response)

# def test_get_leave_requests(app):
#     test_teacher_id = 'T001'
#     with app.test_request_context(path='/', base_url='http://localhost',
#                                   headers={'app': 'wx-app'},
#                                   query_string={'teacher_id': test_teacher_id}):
#         response = get_leave_requests()
#         print(json.loads(response.get_data(as_text=True)))

def test_search_teacher_course(app):
    test_teacher_id = 'T001'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app'},
                                  query_string={'teacher_id': test_teacher_id}):
        response = search_teacher_course()
        print(response)
        print(response[0].json)

def test_review_leave_request(app):
    test_student_id = '2021611011'
    test_course_id = 'c1'
    test_course_no = 14
    test_is_reviewed = 'false'
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers={'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'},
                                  data={'student_id': test_student_id, 'course_id': test_course_id, 'course_no': test_course_no,
                                        'is_reviewed': test_is_reviewed}):
        response = review_leave_request()
        print(response)