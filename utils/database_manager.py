"""
@File   : database_manager.py
@Author : zixian Zhu(hiddensharp)
@Date   : 2023/11/27
@Desc   : 连接MySQL数据库
@Version: version_1
@Last_editor: zixian Zhu
"""

from sqlalchemy import create_engine

class DatabaseManager:
    def __init__(self, table_name, db_user='root', db_password='z20030429', db_host='localhost', db_port=3306, db_name='StudentAttendancnSystemDB', ):
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.engine = create_engine(self._get_connection_string())
        self.df = None

    def _get_connection_string(self):
        return f'mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'