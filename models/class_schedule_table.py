"""
@coding : utf-8
@File   : class_schedule_table.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/19
@Desc   : 课程表信息
@Version: verison_1
@Last_editor zixian Zhu
"""
from utils.database_manager import DatabaseManager
from sqlalchemy import Column, String, text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class ClassSchedule(Base):
    __tablename__ = 'class_schedule'

    schedule_id = Column(Integer, primary_key=True)
    course_id = Column(String)
    day_of_week = Column(String)
    start_week = Column(Integer)
    end_week = Column(Integer)
    start_time = Column(Integer)
    end_time = Column(Integer)

    def __init__(self, schedule_id, course_id, day_of_week, start_week, end_week, start_time, end_time):
        """
        需要传入的参数
        :param schedule_id:安排号
        :param course_id: 课程号
        :param day_of_week: 星期几上课
        :param start_week: 开始上课的周次
        :param end_week: 结束课程的周次
        :param start_time: 开始上课的时间
        :param end_time: 结束上课的时间
        """
        self.schedule_id = schedule_id
        self.course_id = course_id
        self.day_of_week = day_of_week
        self.start_week = start_week
        self.end_week = end_week
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"schedule_id={self.schedule_id},course_id={self.course_id},  " \
               f"day_of_week={self.day_of_week},start_week={self.start_week}, " \
               f"end_week={self.end_week}),start_time={self.start_time}, " \
               f"end_time={self.end_time}"
class ClassScheduleManager:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_manager = DatabaseManager(table_name)

    def add_course(self, schedule):
        '''
        往class_schedule表里面添加记录
        :param schedule:
        :return:
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        existing_class_schedule = session.query(ClassSchedule).filter_by(schedule_id=schedule.schedule_id).first()
        if existing_class_schedule:
            print(f"Schedule with ID {schedule.schedule_id} already exists in the database.")
        else:
            session.add(schedule)
            session.commit()
            print(f"Schedule with ID {schedule.schedule_id} added to the database.")

    def view_all_courses(self):
        '''
        查看class_schedule表中全部的信息
        :return: class_schedule表中全部的信息
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        all_schedule = session.query(ClassSchedule).all()
        for schedule in all_schedule:
            print(schedule)

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
    class_schedule_manager = ClassScheduleManager(table_name='class_schedule')

    #course = Course(course_id="c1", teacher_id="T001", course_name="操作系统原理", teacher_name="张老师")
    #course_manager.add_course(course1)

    class_schedule_manager.view_all_courses()

