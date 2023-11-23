# coding : utf-8
# Author : yuxiang Zeng

import numpy as np
import pandas as pd

from datasets.load_dataset import load_data


class Student:
    def __init__(self, stu_id, stu_name, sex, age, institute, major, class_, dormitory, phone, email, absen_times, leave_times, truany_times):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.sex = sex
        self.age = age
        self.institute = institute
        self.major = major
        self.class_ = class_
        self.dormitory = dormitory
        self.phone = phone
        self.email = email
        self.absen_times = absen_times
        self.leave_times = leave_times
        self.truany_times = truany_times

    def __str__(self):
        return f"Student(stu_id={self.stu_id}, stu_name={self.stu_name}, sex={self.sex}, age={self.age}, " \
               f"institute={self.institute}, major={self.major}, class_={self.class_}, dormitory={self.dormitory}, " \
               f"phone={self.phone}, email={self.email}, absen_times={self.absen_times}, " \
               f"leave_times={self.leave_times}, truany_times={self.truany_times})"


if __name__ == '__main__':
    student1 = Student(stu_id="123456", stu_name="Alice", sex="F", age=20, institute="Engineering", major="Computer Science", class_="CS101", dormitory="D101", phone="1234567890", email="alice@example.com", absen_times=3, leave_times=1, truany_times=2)
    # 打印学生对象的信息
    print(student1)

    df = load_data('学生考勤系统数据库用例表')
    all_student = list()
    for i, data in df.iterrows():
        all_student.append(
            Student(
                stu_id=df['stu_id'],
                stu_name=df['stu_name'],
                sex=df['sex'],
                age=df['age'],
                institute=df['institute'],
                major=df['major'],
                class_=df['class'],
                dormitory=df['dormitory'],
                phone=df['phone'],
                email=df['email'],
                absen_times=df['absen_times'],
                leave_times=df['leave_times'],
                truany_times=df['truany_times']
            )
        )
    print(all_student)
