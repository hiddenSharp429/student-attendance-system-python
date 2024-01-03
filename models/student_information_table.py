"""
@coding : utf-8
@File   : student_information.py
@Author : yuxiang Zeng
@Date   : 2023/11/27
@Desc   : 学生信息表
@Version: version_1
@Last_editor: zixian Zhu
"""

from utils.database_manager import DatabaseManager
from sqlalchemy import Column, String, Integer, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    '''
    将 Student 类与数据库表进行映射
    1.  declarative_base 来定义模型类
    2. Column 来映射到表的列
    '''
    __tablename__ = 'student_information'

    stu_id = Column(String(length=20), primary_key=True)
    stu_name = Column(String)
    sex = Column(String)
    age = Column(Integer)
    institute = Column(String)
    major = Column(String)
    class_no = Column(String)
    dormitory = Column(String)
    phone = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, stu_id, stu_name, sex, age, institute, major, class_no, dormitory, phone, email, password):
        '''
        需要传入的参数
        :param stu_id: 学生的jd
        :param stu_name: 学生的姓名
        :param sex: 学生的性别
        :param age: 学生的年纪
        :param institute: 学生的学院
        :param major:学生的专业
        :param class_no:学生的班级号
        :param dormitory:学生的宿舍号
        :param phone:学生的手机号
        :param email:学生的邮箱
        :param password:学生账号的密码
        '''
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.sex = sex
        self.age = age
        self.institute = institute
        self.major = major
        self.class_no = class_no
        self.dormitory = dormitory
        self.phone = phone
        self.email = email
        self.password = password

    def __str__(self):
        return f"Student(stu_id={self.stu_id}, stu_name={self.stu_name}, sex={self.sex}, age={self.age}, " \
               f"institute={self.institute}, major={self.major}, class_no={self.class_no}, dormitory={self.dormitory}, " \
               f"phone={self.phone}, email={self.email}, password={self.password}"


class StudentManager:
    def __init__(self, table_name):
        '''
        创建一个StudentManager对象时需要传入表的名称（student_information），用于连接数据库中的相关表
        :param table_name:
        '''
        self.table_name = table_name
        self.db_manager = DatabaseManager(table_name)

    def add_student(self, student):
        '''
        插入到student表需要传入一个Student对象
        :param student:
        :return: console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        # Check if the student already exists
        existing_student = session.query(Student).filter_by(stu_id=student.stu_id).first()
        if existing_student:
            print(f"Student with ID {student.stu_id} already exists in the database.")
        else:
            session.add(student)
            session.commit()
            print(f"Student with ID {student.stu_id} added to the database.")

    def view_all_students(self):
        '''
        查看student表中全部的信息
        :return: student表中全部的学生信息
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        all_students = session.query(Student).all()
        for student in all_students:
            print(student)

        return all_students

    def delete_student(self, student_id):
        '''
        删除student表中stu_id为student_id的记录
        :param student_id: 需要删除的学生的id号
        :return: console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        student_to_delete = session.query(Student).filter_by(stu_id=student_id).first()
        if student_to_delete:
            session.delete(student_to_delete)
            session.commit()
            print(f"Student with ID {student_id} deleted from the database.")
        else:
            print(f"Student with ID {student_id} not found in the database.")

    def search_student(self, student_id):
        '''
        查询某个学生的记录，以stu_id为查询条件
        :param student_id: 需要查询的学生id
        :return: 某个学生记录的全部信息
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        student = session.query(Student).filter_by(stu_id=student_id).first()
        if student:
            return student
        else:
            print(f"Student with ID {student_id} not found in the database.")
            return None

    def modify_student(self, student_id, new_data):
        '''
        修改某个学生记录的某些属性列
        :param student_id:需要修改的学生记录的id号
        :param new_data:需要修改的属性列的字典
        :return:console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        student_to_modify = session.query(Student).filter_by(stu_id=student_id).first()
        if student_to_modify:
            for key, value in new_data.items():
                setattr(student_to_modify, key, value)
            session.commit()
            print(f"Student with ID {student_id} modified in the database.")
        else:
            print(f"Student with ID {student_id} not found in the database.")

    def execute_sql_query(self, sql_query):
        '''
        执行任意sql语句
        :param sql_query: 需要在student_information表中执行的sql语句
        :return: 查询的结果
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        result = session.execute(text(sql_query))
        return result.fetchall()

if __name__ == '__main__':
    student_manager = StudentManager(table_name='student_information')

    # student1 = Student(stu_id="2021611012", stu_name="李四", sex="男", age=20, institute="工学院",
    #                    major="计算科学", class_no="1", dormitory="D501", phone="1234567890",
    #                    email="1231@example.com", password="123456")

    #student_manager.add_student(student1)

    student_manager.view_all_students()

    #student_manager.delete_student(student_id="21xxxx")

    #student_manager.search_student(student_id="21xxxx")

    #new_data = {'stu_name': '李四', 'age': 21}
    #student_manager.modify_student(student_id="21xxxx", new_data=new_data)

    #student_manager.view_all_students()
