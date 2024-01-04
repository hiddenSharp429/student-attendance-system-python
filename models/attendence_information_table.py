"""
@coding : utf-8
@File   : attendence_information_table.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/12/7
@Desc   : 考勤信息表
@Version: version_1
@Last_editor
"""

from utils.database_manager import DatabaseManager
from sqlalchemy import Column, String, Integer, DateTime, Time, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class AttendanceRecord(Base):
    __tablename__ = 'attendance_information'

    stu_id = Column(String(length=20), primary_key=True)
    course_id = Column(String, primary_key=True)
    course_no = Column(Integer, primary_key=True)
    teacher_id = Column(String)
    date = Column(DateTime, default=datetime.now())
    status = Column(Integer)
    signin_time = Column(Time)
    signout_time = Column(Time)
    reason = Column(String)

    def __init__(self, stu_id, course_id, course_no, teacher_id, date, status, signin_time=None, signout_time=None, reason=None):
        '''
        :param stu_id: 学生id
        :param course_id: 课程id
        :param course_no: 课程编号
        :param teacher_id: 老师id
        :param date: 上课日期
        :param status: 签到状态 (0 for absent, 1 for present)
        :param signin_time: 签到时间
        :param signout_time: 签退时间
        :param reason: 请假原因
        '''
        self.stu_id = stu_id
        self.course_id = course_id
        self.course_no = course_no
        self.teacher_id = teacher_id
        self.date = date
        self.status = status
        self.signin_time = signin_time
        self.signout_time = signout_time
        self.reason = reason

    def __str__(self):
        return f"AttendanceRecord(stu_id={self.stu_id}, course_id={self.course_id}, " \
               f"course_no={self.course_no}, teacher_id={self.teacher_id}, " \
               f"date={self.date}, status={self.status}, " \
               f"signin_time={self.signin_time}, signout_time={self.signout_time}), reason={self.reason}"


class AttendanceManager:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_manager = DatabaseManager(table_name)

    def add_attendance_record(self, attendance_record):
        '''
        添加考勤记录
        :param attendance_record:
        :return: console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        existing_attendance_record = session.query(AttendanceRecord).filter_by(
            stu_id=attendance_record.stu_id,
            course_id=attendance_record.course_id,
            course_no=attendance_record.course_no
        ).first()

        if existing_attendance_record:
            print(f"This attendance record with stu_id && course_id && course_no"
                  f"{attendance_record.stu_id} && {attendance_record.course_id} && {attendance_record.course_no} "
                  f"already exists in the database.")
        else:
            session.add(attendance_record)
            session.commit()
            print(f"This attendance record with stu_id && course_id && date"
                  f"{attendance_record.stu_id} && {attendance_record.course_id} && {attendance_record.course_no} "
                  f"{attendance_record.teacher_id} && {attendance_record.date} && {attendance_record.status} "
                  f"{attendance_record.signin_time} && {attendance_record.signout_time}"
                  f"added to the database.")

    def view_all_attendance_records(self):
        """
        查看考勤表的全部信息
        :return: attendance_information的全部记录信息
        """
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        all_attendance_records = session.query(AttendanceRecord).all()
        for attendance_record_item in all_attendance_records:
            print(attendance_record_item)

    def search_attendance_record(self, stu_id, course_id, course_no):
        """
        查看某个学生是否签到了
        :param stu_id: 学生的ID
        :param course_id: 课程的ID
        :param course_no: 课程的课次
        :return: Attendance record if found, else None
        """
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        result = session.query(AttendanceRecord).filter_by(
            stu_id=stu_id,
            course_id=course_id,
            course_no=course_no
        ).first()
        # if result.status == 1:
        #     print(f'{result.stu_id}已签到，签到时间为{result.signin_time}')
        # else:
        #     print(f"{result.stu_id}未签到")

        return result

    def execute_sql_query(self, sql_query):
        '''
        执行任意sql语句
        :param sql_query: 需要在attendance_information表中执行的sql语句
        :return: 查询的结果
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        result = session.execute(text(sql_query))

        # 检查语句是更新还是删除
        if sql_query.strip().upper().startswith("UPDATE") or sql_query.strip().upper().startswith("DELETE"):
            row_count = result.rowcount
            print(f"{row_count} row(s) affected.")
            session.commit()  # Commit the transaction
            return row_count

        # 对于其他类型的查询（SELECT、INSERT 等），返回获取的结果
        return result.fetchall()


if __name__ == '__main__':
    attendance_manager = AttendanceManager(table_name='attendance_information')

    # attendance_record = AttendanceRecord(
    #     stu_id="2021611011",
    #     course_id="c1",
    #     course_no=15,
    #     teacher_id="T001",
    #     date=datetime(2023, 1, 1),
    #     status=0
    # )
    # attendance_manager.add_attendance_record(attendance_record)

    # attendance_manager.view_all_attendance_records()
    # attendance_manager.search_attendance_record(2021611001, 'c1', 1)
    # print(attendance_record)

    # sql_query = "SELECT * FROM attendance_information WHERE stu_id = '2021611001' AND course_id = 'c1' AND course_no = 2 AND status = 0"
    # query_result = attendance_manager.execute_sql_query(sql_query)
    # print(query_result)

    # update_sql_query = "UPDATE attendance_information SET status = 2 , reason = '生病请假' WHERE stu_id = '2021611011' AND course_id = 'c1' AND course_no = 17"
    # attendance_manager.execute_sql_query(update_sql_query)