"""
@coding : utf-8
@File   : student_routes.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/17
@Desc   : 有关学生服务的API接口
@Version: version_1
@Last_editor jin Yang
"""
import time
import sys
import os

from flask import jsonify, request, Flask
from flask_cors import CORS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.attendence_information_table import AttendanceManager, AttendanceRecord
from models.class_schedule_table import ClassScheduleManager
from models.course_selection_table import CourseSelectionManager
from models.course_table import CourseManager
from models.post_attendance_table import PostAttendanceManager
from routes import student_routes
from models.student_information_table import StudentManager

from datetime import datetime

CORS(student_routes)


# 验证request请求的header是否合法
def validate_request_headers():
    required_header_value = 'wx-app'

    # 检查请求头中的应用标识
    if 'app' not in request.headers or request.headers['app'] != required_header_value:
        return False

    return True


# 查看所有学生的信息
@student_routes.route('/student_manager/view_all_students', methods=['GET'])
def view_all_students():
    # 创建studentManager的实例
    student_manager = StudentManager(table_name='student')
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


# 查看某个学生某年某周的课程表
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

        course_selection_manager = CourseSelectionManager(table_name='course_selection')
        class_schedule_manager = ClassScheduleManager(table_name='class_schedule')

        # 在course_selection表中查询该学生选择的所有课程号
        sql_query_courses = f"SELECT course_name, course_id FROM course_selection WHERE student_id = '{student_id}' AND semester = '{semester}'"
        course_id_tuples = course_selection_manager.execute_sql_query(sql_query_courses)

        # 将列表转换为列表字典
        course_info_list = [{'course_name': item[0], 'course_id': item[1]} for item in course_id_tuples]

        if not course_info_list:
            return jsonify({'error': 'Student not found or has no selected courses for the specified semester'}), 404

        # 查询符合course_ids的class_schedule记录
        class_schedule_records = []
        for course_info in course_info_list:
            course_id = course_info['course_id']
            course_name = course_info['course_name']
            sql_query_schedule = f"SELECT day_of_week, start_time, end_time FROM class_schedule WHERE course_id = '{course_id}' AND {week_no} BETWEEN start_week AND end_week"
            schedule_records = class_schedule_manager.execute_sql_query(sql_query_schedule)

            schedule_records_with_name = [
                {'course_name': course_name, 'day_of_week': record[0],
                 'start_time': record[1], 'end_time': record[2]} for record in schedule_records]

            class_schedule_records.extend(schedule_records_with_name)

        if class_schedule_records:
            print(class_schedule_records)
            return jsonify({'class_schedule_records': class_schedule_records})
        else:
            return jsonify({'error': 'No class schedule records found for the selected courses'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 验证学生登录信息
@student_routes.route('/student_manager/verify_stu_login', methods=['GET'])
def verify_stu_login():
    # 创建studentManager的实例
    student_manager = StudentManager(table_name='student_information')
    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数
        student_id = request.args.get('student_id')
        student_name = request.args.get('student_name')

        # 查询学生的名字
        stu_name_tuple = student_manager.execute_sql_query(
            f"select stu_name from student_information where stu_id='{student_id}'")
        if not stu_name_tuple:
            return jsonify({'error': 'Student not found'}), 404

        print(stu_name_tuple)
        # 从元组中提取学生姓名
        stu_name = stu_name_tuple[0][0]
        if not stu_name:
            return jsonify({'error': 'Student not found'}), 404

        # 返回学生名字比较的结果
        flag = student_name == stu_name
        if flag == True:
            return jsonify({'msg': str(flag)}), 200
        else:
            return jsonify({'error': 'Student not found'}), 404

    except Exception as e:
        # import traceback
        # print("错误堆栈信息: ", traceback.format_exc())
        return jsonify({'error': str(e)}), 500


# 查看某个学生的信息
@student_routes.route('/student_manager/view_signal_student', methods=['GET'])
def view_signal_student():
    # 创建studentManager的实例
    student_manager = StudentManager(table_name='student_information')
    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数
        student_id = request.args.get('student_id')

        # 使用StudentManger查看所有学生的信息
        signal_student = student_manager.search_student(student_id)
        # 获取没有密码的信息
        info_without_password = {
            "stu_id": signal_student.stu_id,
            "stu_name": signal_student.stu_name,
            "sex": signal_student.sex,
            "age": signal_student.age,
            "institute": signal_student.institute,
            "major": signal_student.major,
            "class_no": signal_student.class_no,
            "dormitory": signal_student.dormitory,
            "phone": signal_student.phone,
            "email": signal_student.email,
        }

        # 返回JSON格式的学生信息
        return jsonify({'student_information': info_without_password})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 学生打卡签到
@student_routes.route('/student_manager/punch_in', methods=['POST'])
def punch_in():
    # 创建CourseManager、PostAttendanceManager、AttendanceManager的实例
    course_manager = CourseManager(table_name='course')
    post_attendance_manager = PostAttendanceManager(table_name='post_attendance')
    attendance_information_manager = AttendanceManager(table_name='attendance_information')

    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数 : 学生ID、打卡时间、签到码
        student_id = request.form.get('student_id')
        punch_in_time = request.form.get('punch_in_time')
        code = request.form.get('code')

        # 根据签到码来查找相关的post_attendance记录
        post_attendance_list = post_attendance_manager.execute_sql_query(f"select * from post_attendance_information"
                                                                         f" where code='{code}'")

        # 判断该考勤任务是否存在
        if len(post_attendance_list) == 0:
            return jsonify({'msg': 'The attendance task does not exist or the check-in code is wrong'}), 404

        # 获取 post_attendance_information 内的考勤时间 %Y-%m-%d %H:%M:%S
        start_time = post_attendance_list[0][4]
        end_time = post_attendance_list[0][5]
        # 获取 post_attendance_information 内的其他信息
        course_id = post_attendance_list[0][1]
        course_no = post_attendance_list[0][3]

        # 获取存入 attendance_information 表的时间  %H:%M:%S
        start_time_str = datetime.strftime(start_time, "%Y-%m-%d %H:%M:%S")
        _, signin_time = start_time_str.split(' ')

        end_time_str = datetime.strftime(end_time, "%Y-%m-%d %H:%M:%S")
        _, signout_time = end_time_str.split(' ')

        # 获取data日期
        data, _ = punch_in_time.split(' ')

        # 获取老师id
        teacher_id = course_manager.execute_sql_query(f"select teacher_id from course where course_id='{course_id}'")
        status = '1'  # 记录考勤状态

        # 封装数据
        attendance_record = AttendanceRecord(
            student_id,
            course_id,
            course_no,
            teacher_id[0][0],
            data,
            status,
            signin_time,
            signout_time
        )

        # 判断打卡签到时间是否在考勤时间区域内
        if time.strptime(start_time_str, "%Y-%m-%d %H:%M:%S") > time.strptime(punch_in_time, "%Y-%m-%d %H:%M:%S") \
                or time.strptime(end_time_str, "%Y-%m-%d %H:%M:%S") < time.strptime(punch_in_time, "%Y-%m-%d %H:%M:%S"):
            # 添加缺勤记录
            attendance_record.status = '0'
            attendance_record.signin_time = None
            attendance_record.signout_time = None
            attendance_information_manager.add_attendance_record(attendance_record)

            return jsonify({'msg': 'This attendance assignment has been terminated'}), 201

        # 添加考勤成功记录
        attendance_information_manager.add_attendance_record(attendance_record)
        return jsonify({'msg': 'The time check is successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 学生发出请假请求
@student_routes.route('/student_manager/absence_on_leave', methods=['POST'])  # 请求创建请假数据
def absence_on_leave():
    # 创建实例
    course_selection_manager = CourseSelectionManager(table_name='course')
    class_schedule_manager = ClassScheduleManager(table_name='class_schedule')
    attendance_manager = AttendanceManager(table_name='attendance_information')
    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数
        student_id = request.form.get('student_id')
        course_id = request.form.get('course_id')
        course_number = request.form.get("course_number")
        reason = request.form.get("reason")

        # 判断课程号是否正确
        sql_command = f"select * from course_selection where student_id = '{student_id}' and course_id = '{course_id}'"
        course_id_decide = course_selection_manager.execute_sql_query(sql_query=sql_command)
        teacher_id = course_id_decide[0][2]  # 获取老师的工号

        if not course_id_decide:
            return jsonify({'error': 'Course id is error'}), 410

        # 判断读取的课次是否正确
        schedule_sql_command = f"select start_week, end_week from class_schedule where course_id = '{course_id}'"
        result_1 = class_schedule_manager.execute_sql_query(schedule_sql_command)
        start_week, end_week = result_1[0]

        if int(course_number) < start_week or int(course_number) > end_week:
            return jsonify({'error': 'course number is error'}), 412

        # 创建请假数据
        attendance_record = AttendanceRecord(stu_id=student_id, course_id=course_id, course_no=course_number,
                                             teacher_id=teacher_id, date=None, status=2, reason=reason)

        result_2 = attendance_manager.search_attendance_record(student_id, course_id, course_number)

        # 当该学生缺勤时
        if(result_2.status == 0):
            update_sql_statement = (f"UPDATE attendance_information SET status = 2, reason = '{reason}' "
                                    f"WHERE stu_id = '{student_id}' AND course_id = '{course_id}' "
                                    f"AND course_no = {course_number}")

            attendance_manager.execute_sql_query(update_sql_statement)

        else:
            # 添加到数据库
            test = attendance_manager.add_attendance_record(attendance_record=attendance_record)
            if test == 0:
                return jsonify({'error': 'record exists in the database'}), 420
            else:
                return jsonify({'successful': 'The leave request was successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 查询学生所选的课程
@student_routes.route('/student_manager/search_student_course', methods=['GET'])  # 请求创建请假数据
def search_student_course():
    # 创建CourseSelectionManager的实例
    course_selection_manager = CourseSelectionManager(table_name='course')
    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取参数请求
        student_id = request.args.get('student_id')

        # 查询数据库
        sql_command = f"select distinct course_name from course_selection where student_id = '{student_id}'"
        all_courses = course_selection_manager.execute_sql_query(sql_query=sql_command)

        # 展开课程名称
        courses_list = [
            {
                'course_name': course.course_name
            }
            for course in all_courses
        ]

        # 返回JSON格式的所选课程
        return jsonify({'student_courses': courses_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    # 创建测试单元的Flask 应用程序
    app = Flask(__name__)

    # # 1. 测试 view_all_students 函数
    # print("Testing view_all_students:")
    # # 构造一个测试请求对象
    # test_request = {'headers': {'app': 'wx-app'}}
    # with app.test_request_context(**test_request):
    #     response = view_all_students()
    #     print(response)

    # 2. 测试 view_student_courses 函数
    # print("\nTesting view_student_courses:")
    # # 提供一些测试参数
    # test_student_id = '2021611001'
    # test_semester = '2023'
    # test_week_no = 5
    # # 构造一个测试请求对象
    # test_request_student_courses = {
    #     'headers': {'app': 'wx-app'},
    #     'args': {'student_id': test_student_id, 'semester': test_semester, 'week_no': test_week_no}  # 使用 args
    # }
    # # 将 args 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_request_student_courses['headers'],
    #                               query_string=test_request_student_courses['args']):  # 使用 query_string 来传递查询参数
    #     response_student_courses = view_student_courses()
    #     print(response_student_courses)

    # 3. 测试 verify_stu_login 函数
    # print("\nTesting verify_stu_login:")
    # # 提供一些测试参数
    # test_student_id_login = '2021611001'
    # test_student_name_login = '代青草'
    # # 构造一个测试请求对象
    # test_request_verify_login = {
    #     'headers': {'app': 'wx-app'},
    #     'args': {'student_id': test_student_id_login, 'student_name': test_student_name_login}  # 使用 args
    # }
    # # 将 args 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_request_verify_login['headers'],
    #                               query_string=test_request_verify_login['args']):  # 使用 query_string 来传递查询参数
    #     response_verify_login = verify_stu_login()
    #     print(response_verify_login)

    # 4. 测试 view_signal_student 函数
    # print("\nTesting view_signal_student:")
    # # 提供一些测试参数
    # test_student_id = '2021611001'
    # # 构造一个测试请求对象
    # test_request_view_signal_student = {
    #     'headers': {'app': 'wx-app'},
    #     'args': {'student_id': test_student_id}  # 使用 args
    # }
    # # 将 args 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_request_view_signal_student['headers'],
    #                               query_string=test_request_view_signal_student['args']):  # 使用 query_string 来传递查询参数
    #     response_view_signal_student = view_signal_student()
    #     print(response_view_signal_student)

    # 5. 测试 punch_in 函数
    # print("\nTesting punch_in:")
    # # 测试参数
    # test_student_id = '2021611011'
    # test_punch_in_time = '2024-01-03 09:20:34'
    # test_code = 'c0003'
    #
    # # 构造一个测试请求对象
    # test_request_punch_in = {
    #     'headers': {'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'},
    #     'data': {'student_id': test_student_id, 'punch_in_time': test_punch_in_time, 'code': test_code}  # 使用data
    # }
    #
    # # 将 data 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_request_punch_in['headers'],
    #                               data=test_request_punch_in['data']):  # 使用 data 来传递 form data
    #     response_punch_in = punch_in()
    #     print(response_punch_in)

    # 6. 测试 absence_on_leave 函数
    # print("\nTesting absence_on_leave:")
    # # 提供一些测试参数
    # test_student_id_leave = '2021611011'
    # test_course_id_leave = 'c1'
    # test_teacher_id_leave = 'T001'
    # test_course_number_leave = 17
    # test_reason = '生病请假'
    # # 构造一个测试请求对象
    # test_request_absence_on_leave = {
    #     'headers': {'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'},
    #     'data': {'student_id': test_student_id_leave,
    #              'course_id': test_course_id_leave,
    #              'teacher_id': test_teacher_id_leave,
    #              'course_number': test_course_number_leave,
    #              'reason': test_reason},  # 使用 data
    # }
    # # 将data 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_request_absence_on_leave['headers'],
    #                               data=test_request_absence_on_leave['data']):  # 使用 data 来传递查询参数
    #     response_absence_on_leave = absence_on_leave()
    #     print(response_absence_on_leave)

    # 7. 测试 search_student_course 函数
    # print("\nTesting search_student_course:")
    # # 提供一些测试参数
    # test_student_id = '2021611003'
    # # 构造一个测试请求对象
    # test_request_search_student_course = {
    #     'headers': {'app': 'wx-app'},
    #     'args': {'student_id': test_student_id}     # 使用 args
    # }
    # # 将args作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_request_search_student_course['headers'],
    #                               query_string=test_request_search_student_course['args']):  # 使用query_string来传递查询参数
    #     response_search_student_course = search_student_course()
    #     print(response_search_student_course)
    #     print(response_search_student_course[0].json)   # 输出返回值的内容
