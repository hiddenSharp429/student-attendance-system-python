"""
@coding : utf-8
@File   : course_selection_table.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/11/30
@Desc   : 学生选课表
@Version: version_1
@Last_editor zixian Zhu
"""
from utils.database_manager import DatabaseManager
from sqlalchemy import Column, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class CourseSelectionRecord(Base):
    __tablename__ = 'course_selection'

    course_id = Column(String(length=20), primary_key=True)
    student_id = Column(String, primary_key=True)
    teacher_id = Column(String)
    course_name = Column(String)
    teacher_name = Column(String)
    semester = Column(String)

    def __init__(self, course_id, student_id, teacher_id, course_name, teacher_name, semester):
        '''
        需要传入的参数
        :param course_id: 课程id
        :param student_id: 学生id
        :param teacher_id: 老师id
        :param course_name: 课程名称
        :param teacher_name: 老师名称
        :param semester: 学年
        '''
        self.course_id = course_id
        self.student_id = student_id
        self.teacher_id = teacher_id
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.semester = semester

    def __str__(self):
        return f"CourseSelectionRecord(course_id={self.course_id}, student_id={self.student_id}, " \
               f"teacher_id={self.teacher_id}, course_name={self.course_name}," \
               f"teacher_name={self.teacher_name}, semester={self.semester})"


class CourseSelectionManager:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_manager = DatabaseManager(table_name)

    def add_course_selection_record(self, course_selection_record):
        '''
        添加学生选课记录
        :param course_selection_record:
        :return:console.log
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        existing_course_selection_record = session.query(CourseSelectionRecord).filter_by(
            course_id=course_selection_record.course_id,
            student_id=course_selection_record.student_id
        ).first()
        if existing_course_selection_record:
            print(f"This course_selection_record with course_id && student_id"
                  f"{course_selection_record.course_id} &&"
                  f"{course_selection_record.student_id} "
                  f"already exists in the database.")
        else:
            session.add(course_selection_record)  # Corrected this line
            session.commit()
            print(f"This course_selection_record with course_id && student_id"
                  f"{course_selection_record.course_id} &&"
                  f"{course_selection_record.student_id} "
                  f"added to the database.")

    def view_all_courses_selection_record(self):
        """
        查看选课表的全部信息
        :return:course_selection的全部记录信息
        """
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()
        all_course_selection_record = session.query(CourseSelectionRecord).all()
        for course_selection_record_item in all_course_selection_record:
            print(course_selection_record_item)

    def execute_sql_query(self, sql_query):
        '''
        执行任意sql语句
        :param sql_query: 需要在course_selection表中执行的sql语句
        :return: 查询的结果
        '''
        Session = sessionmaker(bind=self.db_manager.engine)
        session = Session()

        result = session.execute(text(sql_query))
        return result.fetchall()


if __name__ == '__main__':
    course_selection_manager = CourseSelectionManager(table_name='course_selection')

    # course_selection_record = CourseSelectionRecord(
    #     course_id="c6",
    #     student_id="2021611001",
    #     teacher_id="T002",
    #     course_name="ELC4",
    #     teacher_name="Banana"
    # )
    # course_selection_manager.add_course_selection_record(course_selection_record)

    course_selection_manager.view_all_courses_selection_record()

    # sql_query = "SELECT * FROM course_selection WHERE teacher_id = 'T001'"
    # query_result = course_selection_manager.execute_sql_query(sql_query)
    # print(query_result)
