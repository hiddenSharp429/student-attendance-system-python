"""
@coding : utf-8
@File   : student_routes.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/17
@Desc   : 有关学生服务的API接口
@Version: version_1
@Last_editor
"""

from flask import jsonify, request
from flask_cors import CORS
from routes import student_routes
from models.student_information_table import StudentManager

CORS(student_routes)

# 创建studentManager的实例
student_manager = StudentManager(table_name='student')

# 验证request请求的header是否合法
def validate_request_headers():
    required_header_value = 'wx-app'

    # 检查请求头中的应用标识
    if 'app' not in request.headers or request.headers['app'] != required_header_value:
        return False

    return True

@student_routes.route('/student_manager/view_all_students', methods=['GET'])
def view_all_students():
    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 使用StudentManger查看所有学生的信息
        all_students = student_manager.view_all_students()

        # 展开全部信息
        students_list = [
            {
                'stu_id': student.stu_id,
                'stu_name': student.stu_name,
                'sex': student.sex,
                'age': student.age,
                'institute': student.institute,
                'major': student.major,
                'class_no': student.class_no,
                'dormitory': student.dormitory,
                'phone': student.phone,
                'email': student.email,
                'absen_times': student.absen_times,
                'leave_times': student.leave_times,
                'truany_times': student.truany_times,
                'password': student.password
            }
            for student in all_students
        ]

        # 返回JSON格式的学生信息
        return jsonify({'students': students_list})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@student_routes.route('/student_manager/view_student_courses', methods=['GET'])
def view_student_courses():
    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数
        student_id = request.args.get('student_id')
        semester = request.args.get('semester')
        week_no = request.args.get('week_no')

        # 查询学生信息
        student = StudentManager.search_student(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        # # 查询课程表信息
        # courses = Schedule.query.filter_by(student_id=student.id, semester=semester, week=week).all()
        #
        # # 处理课程表信息
        # course_list = []
        # for course in courses:
        #     course_info = {
        #         'course_name': course.course.name,
        #         'day_of_week': course.day_of_week,
        #         'start_time': course.start_time,
        #         'end_time': course.end_time,
        #     }
        #     course_list.append(course_info)

        return jsonify("待开发中"), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    pass
