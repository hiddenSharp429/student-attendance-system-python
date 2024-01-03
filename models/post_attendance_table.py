"""
@coding : utf-8
@File   : post_attendance_table.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/30
@Desc   : 发布考勤表
@Version: version_1
@Last_editor
"""

from utils.database_manager import DatabaseManager
from sqlalchemy import Column, String, Integer, DateTime, text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()


class PostAttendanceRecord(Base):
    __tablename__ = 'post_attendance_information'

    attendance_id = Column(Integer, primary_key=True)
    course_id = Column(String(length=10))
    course_name = Column(String(length=10))
    course_no = Column(Integer)
    attendance_start_time = Column(DateTime, default=datetime.now())
    attendance_end_time = Column(DateTime, default=datetime.now())
    code = Column(String(length=10))

    def __init__(self, attendance_id, course_id, course_name, course_no, attendance_start_time, attendance_end_time,
                 code):
        '''
        发布考勤记录的构造方法
        :param attendance_id: 考勤ID
        :param course_id: 课程号
        :param course_name: 课程名称
        :param course_no: 课程的周次
        :param attendance_start_time: 考勤的开始时间
        :param attendance_end_time: 考勤的结束时间
        :param code: 签到码
        '''
        self.attendance_id = attendance_id
        self.course_id = course_id
        self.course_name = course_name
        self.course_no = course_no
        self.attendance_start_time = attendance_start_time
        self.attendance_end_time = attendance_end_time
        self.code = code

    def __str__(self):
        return f"PostAttendanceRecord(attendance_id={self.attendance_id}, course_id={self.course_id}, course_name={self.course_name}, " \
               f"course_no={self.course_no}, attendance_start_time={self.attendance_start_time}, " \
               f"attendance_end_time={self.attendance_end_time}, code={self.code})"


class PostAttendanceManager:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_manager = DatabaseManager(table_name)

    def get_max_index(self):
        '''
        获取当前表中的最大索引
        :return: 所有记录中索引的最大值
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        # 使用 func.max 获取 attendance_id 列的最大值
        result = session.query(func.max(PostAttendanceRecord.attendance_id)).scalar()

        # 如果没有记录，返回默认值 0
        return result if result is not None else 0

    def post_attendance(self, post_attendance_record):
        '''
        发布考勤
        :param post_attendance_record: 发布考勤的记录
        :return: console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        existing_post_attendance_record = session.query(PostAttendanceRecord).filter_by(
            code=post_attendance_record.code,
        ).first()

        if existing_post_attendance_record:
            print(f"This post attendance record with code '{post_attendance_record.code}' already exists in the database.")
            return False

        else:
            session.add(post_attendance_record)
            session.commit()
            print(f"This post attendance record with attendance_id"
                  f"{post_attendance_record.attendance_id} && {post_attendance_record.course_id} &&{post_attendance_record.course_name}"
                  f"{post_attendance_record.course_no} && {post_attendance_record.attendance_start_time}"
                  f"{post_attendance_record.attendance_end_time} && {post_attendance_record.code}"
                  f"added to the database.")
            return True

    def view_all_post_attendance_records(self):
        """
        查看发布考勤表的全部信息
        :return: post_attendance_information的全部记录信息
        """
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        all_post_attendance_records = session.query(PostAttendanceRecord).all()
        for post_attendance_record_item in all_post_attendance_records:
            print(post_attendance_record_item)

    def search_post_attendance_record(self, attendance_id):
        """
        查看某个考勤是否发布了
        :param attendance_id: 考勤号
        :return: post attendance record if found, else None
        """
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        result = session.query(PostAttendanceRecord).filter_by(
            attendance_id=attendance_id,
        ).first()

        if result != None:
            print(f'{result.attendance_id}已存在')
        else:
            print(f"{attendance_id}查找不到")

    def execute_sql_query(self, sql_query):
        '''
        执行任意sql语句
        :param sql_query: 需要在attendance_information表中执行的sql语句
        :return: 查询的结果
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        result = session.execute(text(sql_query))
        return result.fetchall()


if __name__ == '__main__':
    post_attendance_manager = PostAttendanceManager(table_name='post_attendance_information')

    # one_day = timedelta(days=1)
    # max_index = post_attendance_manager.get_max_index()  # 获取最大索引号
    # new_index = max_index + 1  # 新记录的索引号
    #
    # post_attendance_record = PostAttendanceRecord(
    #     attendance_id=new_index,
    #     course_id='c1',
    #     course_name='操作系统原理',
    #     course_no=18,
    #     attendance_start_time=datetime.now(),
    #     attendance_end_time=datetime.now() + one_day,
    #     code='c0001'
    # )
    # post_attendance_manager.post_attendance(post_attendance_record)

    # post_attendance_manager.view_all_post_attendance_records()

    # post_attendance_manager.search_post_attendance_record(3)

    # sql_query = "SELECT * FROM post_attendance_information Where course_name = '操作系统原理'"
    # query_result = post_attendance_manager.execute_sql_query(sql_query)
    # print(query_result)
