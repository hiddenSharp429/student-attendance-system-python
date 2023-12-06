"""
@coding : utf-8
@File   : app.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/6
@Desc   : Flask服务
@Version: version_1
@Last_editor zixian Zhu
"""

from flask import Flask, jsonify
from table.student_information_table import StudentManager

app = Flask(__name__)

# 创建studentManager的实例
student_manager = StudentManager(table_name='student')

@app.route('/student_manager/view_all_students', methods=['GET'])
def view_all_students():
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

