"""
@coding : utf-8
@File   : teacher_information.py
@Author : yuxiang Zeng
@Date   : 2023/11/27
@Desc   : 老师信息表
@Version: version_1
@Last_editor: zixian Zhu
"""

from utils.database_manager import DatabaseManager
from sqlalchemy import Column, String, Integer, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Teacher(Base):
    '''
    将 Teacher 类与数据库表进行映射
    1.  declarative_base 来定义模型类
    2. Column 来映射到表的列
    '''
    __tablename__ = 'teacher_information'

    teacher_id = Column(String(length=20), primary_key=True)
    teacher_name = Column(String)
    sex = Column(String)
    age = Column(Integer)
    institute = Column(String)
    major = Column(String)
    email = Column(String)
    phone_number = Column(String)
    office = Column(String)
    home = Column(String)
    password = Column(String)

    def __init__(self, teacher_id, teacher_name, sex, age, institute, major, email, phone_number, office, home,
                 password):
        '''
        需要传入的参数
        :param teacher_id: 教师的id
        :param teacher_name:教师的姓名
        :param sex:性别
        :param age:年龄
        :param institute:所属学院
        :param major:专业
        :param email:电子邮件
        :param phone_number:电话号码
        :param office:办公室地点
        :param home:居住地址
        :param password:账号密码
        '''
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.sex = sex
        self.age = age
        self.institute = institute
        self.major = major
        self.email = email
        self.phone_number = phone_number
        self.office = office
        self.home = home
        self.password = password

    def __str__(self):
        return f"Teacher(teacher_id={self.teacher_id}, teacher_name={self.teacher_name}, sex={self.sex}, age={self.age}, " \
               f"institute={self.institute}, major={self.major}, email={self.email}, " \
               f"phone_number={self.phone_number}, office={self.office}, home={self.home}), password={self.password}"


class TeacherManager:
    def __init__(self, table_name):
        '''
        创建一个TeacherManager对象时需要传入表的名称（teacher_information），用于连接数据库中的相关表
        :param table_name:
        '''
        self.table_name = table_name
        self.db_manager = DatabaseManager(table_name)

    def add_teacher(self, teacher):
        '''
        插入到teacher表需要传入一个teacher对象
        :param teacher:
        :return: console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        # Check if the teacher already exists
        existing_teacher = session.query(Teacher).filter_by(teacher_id=teacher.teacher_id).first()
        if existing_teacher:
            print(f"teacher with ID {teacher.teacher_id} already exists in the database.")
        else:
            session.add(teacher)
            session.commit()
            print(f"teacher with ID {teacher.teacher_id} added to the database.")

    def view_all_teachers(self):
        '''
        查看teacher表中全部的信息
        :return: teacher表中全部的教师信息
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        all_teachers = session.query(Teacher).all()
        for teacher in all_teachers:
            print(teacher)

    def delete_teacher(self, teacher_id):
        '''
        删除teacher表中teacher_id为teacher_id的记录
        :param teacher_id: 需要删除的老师的id号
        :return: console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        teacher_to_delete = session.query(Teacher).filter_by(teacher_id=teacher_id).first()
        if teacher_to_delete:
            session.delete(teacher_to_delete)
            session.commit()
            print(f"teacher with ID {teacher_id} deleted from the database.")
        else:
            print(f"teacher with ID {teacher_id} not found in the database.")

    def search_teacher(self, teacher_id):
        '''
        查询某个老师的记录，以teacher_id为查询条件
        :param teacher_id: 需要查询的老师id
        :return: 某个老师记录的全部信息
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        teacher = session.query(Teacher).filter_by(teacher_id=teacher_id).first()
        if teacher:
            print(teacher)
            return teacher

        else:
            print(f"teacher with ID {teacher_id} not found in the database.")
            return None

    def modify_teacher(self, teacher_id, new_data):
        '''
        修改某个老师记录的某些属性列
        :param teacher_id:需要修改的老师记录的id号
        :param new_data:需要修改的属性列的字典
        :return:console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        teacher_to_modify = session.query(Teacher).filter_by(teacher_id=teacher_id).first()
        if teacher_to_modify:
            for key, value in new_data.items():
                setattr(teacher_to_modify, key, value)
            session.commit()
            print(f"teacher with ID {teacher_id} modified in the database.")
        else:
            print(f"teacher with ID {teacher_id} not found in the database.")

    def execute_sql_query(self, sql_query):
        '''
        执行任意sql语句
        :param sql_query: 需要在teacher_information表中执行的sql语句
        :return: 查询的结果
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        result = session.execute(text(sql_query))
        return result.fetchall()


if __name__ == '__main__':
    teacher_manager = TeacherManager(table_name='teacher_information')

    teacher1 = Teacher(teacher_id="T008", teacher_name="Dr.Smith", sex="男", age=40, institute="计算机",
                       major="计算机科学与计算", email="8@example.com",
                       phone_number="12345678908", office="OfficeF", home="HomeF", password="123456")

    # teacher_manager.add_teacher(teacher1)

    # teacher_manager.view_all_teachers()

    # teacher_manager.delete_teacher(teacher_id="21xxxx")

    # teacher_manager.search_teacher(teacher_id="21xxxx")

    # new_data = {'stu_name': '李四', 'age': 21}
    # teacher_manager.modify_teacher(teacher_id="21xxxx", new_data=new_data)

    # teacher_manager.view_all_teachers()

    sql_query = "SELECT * FROM teacher_information WHERE teacher_id = 'T001'"
    result = teacher_manager.execute_sql_query(sql_query)
    print(result)