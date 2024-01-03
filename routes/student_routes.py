"""
@coding : utf-8
@File   : student_routes.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/17
@Desc   : 有关学生服务的API接口
@Version: version_1
@Last_editor jin Yang
"""

from flask import jsonify, request, Flask
from flask_cors import CORS

from models.class_schedule_table import ClassScheduleManager
from models.course_selection_table import CourseSelectionManager
from routes import student_routes
from models.student_information_table import StudentManager

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
    student_manager = StudentManager(table_name='student')
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




if __name__ == "__main__":
    # 创建测试单元的Flask 应用程序
    app = Flask(__name__)

    # 1. 测试 view_all_students 函数
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