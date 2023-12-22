"""
@coding : utf-8
@File   : course_table.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/11/30
@Desc   : 
@Version: version_1
@Last_editor zixian Zhu
"""

from utils.database_manager import DatabaseManager
from sqlalchemy import Column, String, text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'

    course_id = Column(String(length=20), primary_key=True)
    teacher_id = Column(String)
    course_name = Column(String)
    teacher_name = Column(String)

    def __init__(self, course_id, teacher_id, course_name, teacher_name):
        '''
        需要传入的参数
        :param course_id: 课程id
        :param teacher_id: 老师id
        :param course_name: 课程名称
        :param teacher_name: 老师名称
        '''
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.course_name = course_name
        self.teacher_name = teacher_name

    def __str__(self):
        return f"CourseSelectionRecord(course_id={self.course_id},teacher_id={self.teacher_id},  " \
               f"course_name={self.course_name},teacher_name={self.teacher_name}"
class CourseManager:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_manager = DatabaseManager(table_name)

    def add_course(self, course):
        '''

        :param course:
        :return:
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        existing_course = session.query(Course).filter_by(course_id=course.course_id).first()
        if existing_course:
            print(f"Student with ID {course.course_id} already exists in the database.")
        else:
            session.add(course)
            session.commit()
            print(f"Student with ID {course.course_id} added to the database.")

    def view_all_courses(self):
        '''
        查看student表中全部的信息
        :return: student表中全部的学生信息
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        all_course = session.query(Course).all()
        for course in all_course:
            print(course)

    def execute_sql_query(self, sql_query):
        '''
        执行任意sql语句
        :param sql_query: 需要在course表中执行的sql语句
        :return: 查询的结果
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        result = session.execute(text(sql_query))
        return result.fetchall()


if __name__ == '__main__':
    course_manager = CourseManager(table_name='course')

    #course = Course(course_id="c1", teacher_id="T001", course_name="操作系统原理", teacher_name="张老师")
    #course_manager.add_course(course1)

    course_manager.view_all_courses()
