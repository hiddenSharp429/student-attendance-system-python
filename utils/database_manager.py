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
    def __init__(self, table_name, db_user='ubuntu', db_password='i3^N9g&uz', db_host='43.136.80.11', db_port=3306, db_name='db', ):
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