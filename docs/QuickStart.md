<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-02 10:12:23
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 18:12:15
 * @FilePath: /Student Attendance System/docs/QuickStart.md
 * @Description: 快速开始
-->

# 快速开始

这个项目是前后端分离的，前端是用微信原生语法写的微信小程序，后端是用Python的Flask框架写的服务端，下面我们将从后端部署开始～

## 1. 后端Flask的快速部署

在这部分你需要有：

> 1. MySql 8.3.0
> 2. conda环境
> 3. 一个数据库管理工具（以Navicat为例）

你准备了以上工具后，我们就开始部署吧～

### 1.1 数据库快速导入

1. 打开Navicat选择本地连接，新建一个数据库
>注:建议新建的数据库名为“StudentAttendancnSystemDB”，不然请自行修改utils\database_manager.py里面的db_name

2. 右键该新建的数据库，在选择栏中选择“运行SQL文件”

3. 依次导入sql文件夹中的init文件夹下所有sql文件，如：sql/init/xxx.sql

### 1.2 虚拟环境的创建

1. 在Terminal中创建一个新的conda虚拟环境，名为Flask。`conda create -name python=3.8`
2. 激活新建的虚拟环境。`conda activate Flask`
3. 安装该项目的所有依赖 `conda install --file requirements.txt`或者`mamba install --file requirements.txt`


### 1.3 数据库连接文件修改
1. 在utils文件夹中找到database_manager.py文件
2. 修改__init_函数的参数中的`db_user`/`db_password`/`db_host`等参数
```
 def __init__(self, table_name, db_user='your_user', db_password='your_password', db_host='127.0.0.1', db_port=3306, db_name='StudentAttendancnSystemDB', ):
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.engine = create_engine(self._get_connection_string())
        self.df = None
```
注：这里的`db_name`参数可以不用改，假如前面是按照该名称创建的数据库

完成上述步骤就可以启动后端了，在terminal中输入`python app.py`启动后端。返回如下信息则为开启服务成功
```
Flask app is running on http://0.0.0.0:5000
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.43.207:5000
Press CTRL+C to quit
```
### 1.4 进行端口测试
测试文件放在了test文件夹下，里面有两个路由测试文件，学生路由和老师路由的～
```
Student Attendance System/
│
├── app.py
.......
├── test/
│   ├── test_teacher_routes.py
│   └── test_student_routes.py
```
使用pytest来进行路由端口测试，使用`pytest test/test_student_routes.py`来测试学生路由的端口是否正常，老师路由同理。通过的返回信息如下
```
(Flask) hiddensharp429@ZixiandeMBP Student Attendance System % pytest test/test_student_routes.py
============================================================== test session starts ==============================================================
platform darwin -- Python 3.8.19, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/hiddensharp429/Code/PYTHON/Student Attendance System
collected 7 items                                                                                                                               

test/test_student_routes.py .......                                                                                                       [100%]

=============================================================== warnings summary ================================================================
models/attendence_information_table.py:17
  /Users/hiddensharp429/Code/PYTHON/Student Attendance System/models/attendence_information_table.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

models/class_schedule_table.py:15
  /Users/hiddensharp429/Code/PYTHON/Student Attendance System/models/class_schedule_table.py:15: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

models/course_selection_table.py:15
  /Users/hiddensharp429/Code/PYTHON/Student Attendance System/models/course_selection_table.py:15: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

models/course_table.py:16
  /Users/hiddensharp429/Code/PYTHON/Student Attendance System/models/course_table.py:16: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

models/post_attendance_table.py:17
  /Users/hiddensharp429/Code/PYTHON/Student Attendance System/models/post_attendance_table.py:17: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

models/student_information_table.py:16
  /Users/hiddensharp429/Code/PYTHON/Student Attendance System/models/student_information_table.py:16: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================================================= 7 passed, 6 warnings in 0.28s =========================================================
```
显示全部都是passed的即为通过测试。

## 2. 前端wx—miniprogram的快速部署
### 2.1 注册帐号(可选)以及工具安装
1. 小程序开发的第一步，是去微信公众平台注册，申请一个 AppID，这是免费的。
>注：这步不是必须的，假如不是自己想开发一个微信小程序，可以直接使用测试号，不需要自己注册一个AppID
2. 下载微信提供的小程序开发工具。这个工具是必需的，因为只有它才能运行和调试小程序源码。
>注：开发者工具支持 Windows 和 MacOS 两个平台。我装的是 MacOS （64位）的版本'
3. 安装好打开这个软件，会要求你使用微信扫描二维码登录。
4. 登录后，进入新建项目的页面，点击右侧的+号，就跳出了新建小程序的页面。

### 2.2 导入项目
1. 我们需要导入项目文件里的`Miniprogram`文件
2. 可以选择用自己的AppID或者测试号
3. 进入开发工具页面，完成项目导入

### 2.3 测试登陆
1. 在首页输入测试帐号`2021611011`
2. 在首页输入测试姓名“张三” 
3. 点击登陆后查看是否成功，若不成功请查看API文档中的相关的API错误码说明