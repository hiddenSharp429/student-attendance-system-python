# coding : utf-8
# Author : yuxiang Zeng

import numpy as np
import pandas as pd


class Teacher:
    def __init__(self, teacher_id, teacher_name, sex, age, institute, major, class_number, email, phone_number, office, home):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.sex = sex
        self.age = age
        self.institute = institute
        self.major = major
        self.class_number = class_number
        self.email = email
        self.phone_number = phone_number
        self.office = office
        self.home = home

    def __str__(self):
        return f"Teacher(teacher_id={self.teacher_id}, teacher_name={self.teacher_name}, sex={self.sex}, age={self.age}, " \
               f"institute={self.institute}, major={self.major}, class_number={self.class_number}, email={self.email}, " \
               f"phone_number={self.phone_number}, office={self.office}, home={self.home})"


if __name__ == '__main__':
    teacher1 = Teacher(teacher_id="T001", teacher_name="Dr. Smith", sex="M", age=40, institute="Engineering",
                       major="Computer Science", class_number="CS101", email="smith@example.com",
                       phone_number="1234567890", office="Room 101", home="123 Main St")
    print(teacher1)
