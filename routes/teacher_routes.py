"""
@coding : utf-8
@File   : teacher_routes.py
@Author : jin Yang()
@Date   : 2023/12/18
@Desc   : 有关老师服务的API接口
@Version: version_1
@Last_editor Zixian Zhu
"""
from datetime import datetime, timedelta

from flask import jsonify, request, Flask
from flask_cors import CORS

from models.attendence_information_table import AttendanceManager
from models.course_selection_table import CourseSelectionManager
from models.post_attendance_table import PostAttendanceManager, PostAttendanceRecord
from routes import teacher_routes
from models.teacher_information_table import TeacherManager

CORS(teacher_routes)



# 验证request请求的header是否合法
def validate_request_headers():
    required_header_value = 'wx-app'

    # 检查请求头中的应用标识
    if 'app' not in request.headers or request.headers['app'] != required_header_value:
        return False

    return True

# 验证老师登录信息
@teacher_routes.route('/teacher_manager/verify_teacher_login', methods=['GET'])
def verify_teacher_login():
    # 创建teacherManager的实例
    teacher_manager = TeacherManager(table_name='teacher')
    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数
        teach_id = request.args.get('teacher_id')
        teach_name = request.args.get('teacher_name')

        # 查询老师的名字
        teacher_name_tuple = teacher_manager.execute_sql_query(
            f"select teacher_name from teacher_information where teacher_id='{teach_id}'")

        # 从元组中提取老师姓名
        teacher_name = teacher_name_tuple[0][0]
        if not teacher_name:
            return jsonify({'error': 'Teacher not found'}), 404

        # 返回学生名字比较的结果
        flag = teach_name == teacher_name
        if flag==True:
            return jsonify({'msg': str(flag)}) ,200
        else:
            return jsonify({'error': 'Teacher not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 老师查看特定课程特定周次的缺勤名单
@teacher_routes.route('/teacher_manager/view_absentee_list', methods=['GET'])
def view_absentee_list():
    # 创建查询管理器实例
    course_selection_manager = CourseSelectionManager(table_name='course_selection')
    attendance_manager = AttendanceManager(table_name='attendence_information')
    # 验证请求头部
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数：课程号和周次
        course_id = request.args.get('course_id')
        course_no = request.args.get('course_no')

        # 查询选定课程的所有学生
        sql_query_students = f"select student_id from course_selection where course_id = '{course_id}'"
        student_ids = course_selection_manager.execute_sql_query(sql_query_students)


        # 存储缺勤学生的信息
        absent_students = []

        # 检查每个学生在指定周次的出勤情况
        for student_id_tuple in student_ids:
            student_id = student_id_tuple[0]
            sql_query_absence = f"SELECT stu_id FROM attendance_information WHERE stu_id = '{student_id}' AND course_id = '{course_id}' AND course_no = {course_no} AND status = 0"
            absence_count = attendance_manager.execute_sql_query(sql_query_absence)

            # 如果学生在该周次有缺勤记录，则添加到列表中
            if len(absence_count) != 0:
                absent_students.append(student_id)

        # 返回缺勤学生名单
        return jsonify({'absent_students': absent_students}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 老师发布考勤
@teacher_routes.route('/teacher_manager/post_attendance', methods=['POST'])
def post_attendance():
    # 创建查询管理器实例
    post_attendance_manager = PostAttendanceManager(table_name='post_attendance_information')

    # 验证请求头部
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数：课程号和周次
        course_name = request.form.get('course_name')
        course_id = request.form.get('course_id')
        course_no = request.form.get('course_no')
        attendance_start_time = request.form.get('attendance_start_time')
        attendance_end_time = request.form.get('attendance_end_time')
        code = request.form.get('code')

        max_index = post_attendance_manager.get_max_index()  # 获取最大索引号
        new_index = max_index + 1  # 新记录的索引号

        # 创建post_attendance记录
        post_attendance_record = PostAttendanceRecord(
            attendance_id=new_index,
            course_id=course_id,
            course_name=course_name,
            course_no=course_no,
            attendance_start_time=attendance_start_time,
            attendance_end_time=attendance_end_time,
            code=code
        )

        if post_attendance_manager.post_attendance(post_attendance_record):
            # 返回缺勤学生名单
            return jsonify({'msg':'发布考勤成功'}), 200



    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 查看某个学生的信息
@teacher_routes.route('/teacher_manager/view_signal_teacher', methods=['GET'])
def view_signal_teacher():
    teacher_manager = TeacherManager(table_name='teacher_information')

    # 验证请求头
    if not validate_request_headers():
        return jsonify({'error': 'Invalid application identification'}), 400

    try:
        # 获取请求参数
        teacher_id = request.args.get('teacher_id')

        # 使用StudentManger查看所有学生的信息
        signal_teacher = teacher_manager.search_teacher(teacher_id)

        # 获取没有密码的信息
        info_without_password = {
            "teacher_id": signal_teacher.teacher_id,
            "teacher_name": signal_teacher.teacher_name,
            "sex": signal_teacher.sex,
            "age": signal_teacher.age,
            "institute": signal_teacher.institute,
            "major": signal_teacher.major,
            "office": signal_teacher.office,
            "home": signal_teacher.home,
            "phone_number": signal_teacher.phone_number,
            "email": signal_teacher.email,
        }

        # 返回JSON格式的学生信息
        return jsonify({'teacher_information': info_without_password})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    # 创建测试单元的Flask 应用程序
    app = Flask(__name__)

    #  1. 测试 verify_stu_login 函数
    # print("\nTesting verify_stu_login:")
    # 提供一些测试参数
    # test_teacher_id_login = 'T001'
    # test_teacger_name_login = '张老师'
    # # 构造一个测试请求对象
    # test_request_verify_login = {
    #     'headers': {'app': 'wx-app'},
    #     'args': {'teacher_id': test_teacher_id_login, 'teacher_name': test_teacger_name_login}  # 使用 args
    # }
    # # 将 args 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_request_verify_login['headers'],
    #                               query_string=test_request_verify_login['args']):  # 使用 query_string 来传递查询参数
    #     response_verify_login = verify_teacher_login()
    #     print(response_verify_login)


    # 2. 测试 view_absentee_list 函数
    # print("\nTesting view_absentee_list:")
    # # 提供一些测试参数
    # test_course_id = 'c1'
    # test_course_no = 2
    # # 构造一个测试请求对象
    # test_view_absentee_list = {
    #     'headers': {'app': 'wx-app'},
    #     'args': {'course_id': test_course_id, 'course_no': test_course_no}  # 使用 args
    # }
    # # 将 args 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_view_absentee_list['headers'],
    #                               query_string=test_view_absentee_list['args']):  # 使用 query_string 来传递查询参数
    #     response_view_absentee_list = view_absentee_list()


    # 3. 测试 post_attendance 函数
    # print("\nTesting post_attendance:")
    #
    # one_day = timedelta(days=1)
    #
    # # 提供一些测试参数
    # test_course_name = '操作系统原理'
    # test_course_id = 'c1'
    # test_course_no = 17
    # test_attendance_start_time = datetime.now()
    # test_attendance_end_time = datetime.now() + one_day
    # test_code = 'c0002'
    #
    # # 构造一个测试请求对象
    # test_post_attendance = {
    #     'headers': {'app': 'wx-app'},
    #     'args': {'course_name': test_course_name, 'course_id': test_course_id, 'course_no':test_course_no, 'attendance_start_time': test_attendance_start_time, 'attendance_end_time':test_attendance_end_time, 'code':test_code}  # 使用 args
    # }
    # # 将 args 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_post_attendance['headers'],
    #                               query_string=test_post_attendance['args']):  # 使用 query_string 来传递查询参数
    #     response_post_attendance = post_attendance()


    # 4. 测试 view_signal_teacher 函数
    # print("\nTesting view_signal_teacher:")
    # # 提供一些测试参数
    # test_teacher_id = 'T001'
    # # 构造一个测试请求对象
    # test_request_view_signal_teacher = {
    #     'headers': {'app': 'wx-app'},
    #     'args': {'teacher_id': test_teacher_id}  # 使用 args
    # }
    # # 将 args 作为构造请求上下文的一部分
    # with app.test_request_context(path='/', base_url='http://localhost',
    #                               headers=test_request_view_signal_teacher['headers'],
    #                               query_string=test_request_view_signal_teacher['args']):  # 使用 query_string 来传递查询参数
    #     response_view_signal_teacher = view_signal_teacher()
    #     print(response_view_signal_teacher)