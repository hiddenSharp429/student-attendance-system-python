"""
@File   : save_table.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/11/27
@Desc   : 将本地的excel或者csv表存入数据库
@Version: version_1
@Last_editor: zixian Zhu
"""

import pandas as pd
from sqlalchemy import create_engine

# 读取文件的名称
file_name_1 = '学生考勤系统数据库用例表.xlsx'
file_name_2 = ''

# 将要存入数据库中的表名称
table_name_1 = ''
table_name_2 = ''
table_name_3 = ''

file_path = file_name_1
df = pd.read_excel(file_path)

print(df)

# 连接到远程数据库
db_user = 'ubuntu'
db_password = 'i3^N9g&uz'
db_host = '43.136.80.11'
db_port = 3306
db_name = 'db'

# 连接引擎
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
print(engine)

# 将数据存入数据库
df.to_sql(table_name_1, engine, index=True, if_exists='replace')

print(f'Data has been successfully loaded into the {table_name_1} table in the remote database.')
