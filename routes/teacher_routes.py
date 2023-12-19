"""
@coding : utf-8
@File   : teacher_routes.py
@Author : jin Yang()
@Date   : 2023/12/18
@Desc   : 有关老师服务的API接口
@Version: version_1
@Last_editor Zixian Zhu
"""

from flask import jsonify, request, Flask
from flask_cors import CORS
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


if __name__ == "__main__":
    # 创建测试单元的Flask 应用程序
    app = Flask(__name__)

    #  1. 测试 verify_stu_login 函数
    print("\nTesting verify_stu_login:")
    # 提供一些测试参数
    test_teacher_id_login = 'T001'
    test_teacger_name_login = '张老师'
    # 构造一个测试请求对象
    test_request_verify_login = {
        'headers': {'app': 'wx-app'},
        'args': {'teacher_id': test_teacher_id_login, 'teacher_name': test_teacger_name_login}  # 使用 args
    }
    # 将 args 作为构造请求上下文的一部分
    with app.test_request_context(path='/', base_url='http://localhost',
                                  headers=test_request_verify_login['headers'],
                                  query_string=test_request_verify_login['args']):  # 使用 query_string 来传递查询参数
        response_verify_login = verify_teacher_login()
        print(response_verify_login)
