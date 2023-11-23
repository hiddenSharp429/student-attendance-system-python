# coding : utf-8
# Author : yuxiang Zeng
from datasets.load_dataset import load_data

import pandas as pd

# 定义学生信息表
columns = [
    'stu_id', 'stu_name', 'sex', 'age', 'institute', 'major', 'class_',
    'dormitory', 'phone', 'email', 'absen_times', 'leave_times', 'truany_times'
]


if __name__ == '__main__':
    dataFrame = pd.DataFrame([], columns=columns)
    print(dataFrame)
    df = load_data('学生考勤系统数据库用例表')
