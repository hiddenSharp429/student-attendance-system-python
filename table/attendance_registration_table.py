# coding : utf-8
# Author : yuxiang Zeng

import numpy as np
import pandas as pd

class Attendance:
    def __init__(self, stu_id, class_id, class_time, stu_name, teac_id, lea1_or_tru0):
        self.stu_id = stu_id
        self.class_id = class_id
        self.class_time = class_time
        self.stu_name = stu_name
        self.teac_id = teac_id
        self.lea1_or_tru0 = lea1_or_tru0

    def __str__(self):
        return f"Attendance(stu_id={self.stu_id}, class_id={self.class_id}, class_time={self.class_time}, " \
               f"stu_name={self.stu_name}, teac_id={self.teac_id}, lea1_or_tru0={self.lea1_or_tru0})"


if __name__ == '__main__':
    attendance1 = Attendance(stu_id="123456", class_id="CS101", class_time=1, stu_name="Alice", teac_id="T001", lea1_or_tru0="1")
    print(attendance1)
