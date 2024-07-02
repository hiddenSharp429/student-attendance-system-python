<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-01 19:16:18
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 18:28:24
 * @FilePath: /Student Attendance System/docs/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 学生考勤系统（微信小程序原生语法+Flask框架）
## 1. 😝简介
该项目名称是“学生考勤系统”，其是一款基于微信小程序和Flask框架开发的应用，旨在帮助学校管理学生的考勤和课程信息。系统通过集成数据库管理、API开发以及前后端交互，实现了便捷的学生考勤记录、课程表管理和教师交互功能。其主要特点包括：
1. 微信小程序支持：利用微信小程序的原生语法开发，提供便捷的移动端访问和用户体验。
2. Flask框架后端：采用Python Flask框架搭建强大的后端服务，支持多种API接口的开发和管理。
3. 多功能模块：包括学生考勤记录、课程表管理、教师考勤发布及审核等功能，满足学校日常管理需求。
4. 数据库集成：支持与远程MySQL数据库的连接，实现数据的安全存储和高效管理。
5. 持续更新与改进：系统在不断更新和改进中，通过版本迭代新增功能、优化性能，并修复已知问题，以提升系统的稳定性和用户满意度。

该系统旨在为学校教务管理提供现代化、智能化的解决方案，促进学生出勤管理和课程信息管理的效率和透明度。这个也是我们当时软件工程所交的期末大作业，可能有些许不合理的地方，不过请放心食用！～
## 2. 更新日志
### 版本 0.1.0 (2023.11.27下午)

```angular2html
@Author : zixian Zhu
@Date   : 2023/11/27
@Submit_branch: version_1
```

#### 新特性

- [功能1]：连接了远程服务器中的MySQL。
- [功能2]：student_information_table.py新增一个StudentManager类，用于学生表中的增删改查。

#### 改进

- [改进1]：将读取本地的excel文件修改成了读取远程服务器上的数据库。
- [改进2]：完善了文件头和函数注释等细节。

#### 修复

- [修复1]：修改原本的表名称student(student_information)。
- [修复2]：修改了原本表student中的class属性列(class_no)，原因是class为保留关键字。

### 版本 0.2.0 (2023.11.27晚上)

```angular2html
@Author : zixian Zhu
@Date   : 2023/11/27
@Submit_branch: version_1
```

#### 新特性

- [功能1]：teacher_information_table.py新增一个TeacherManager类，用于老师表中的增删改查。

#### 改进

- [改进1]：修改了表的结构，具体详情请看文档。
- [改进2]：将各个表的测试数据都上传到了远程数据库中。

#### 修复

无

### 版本 0.3.0 (2023.11.30晚上)

```angular2html
@Author : zixian Zhu
@Date   : 2023/11/30
@Submit_branch: version_1
```

#### 新特性

- [功能1]：新增course_selection_table.py文件，该文件 
  包含CourseSelectionRecord、CourseSelectionManager这两个类，用于学生选课表course_selection
  中的查询操作
  
- [功能2]：新增了course.py文件，该文件包含Course、CourseManager两个类，用于课程表的中的相关操作
  
- [功能3]：每个表的Manager类都新增了对外提供的查询函数`execute_sql_query(self, sql_query)`
  可以查询任意内容。
  
#### 改进
  
- [改进1]：修改了course的表名称, course->course_seleciton
  
- [改进2]：新增了课程表course，用于记录课程的相关信息
  

#### 修复

无

### 版本 0.4.0 (2023.12.6晚上)

```angular2html
@Author : zixian Zhu
@Date   : 2023/12/6
@Submit_branch: version_1
```

#### 新特性

- [功能1]：删除原来的main.py，新增一个app.py，app.py中提供了一个简单的后端调用接口，用于获取所有学生信息。
- [功能2]：docs文件夹新增一个api调用的模板文档(api_template.md)和一个api交流文档(api.md)

#### 改进

无

#### 修复

无

### 版本 0.5.0 (2023.12.7)

```angular2html
@Author : zixian Zhu
@Date   : 2023/12/7
@Submit_branch: version_1
```

#### 新特性

- [功能1]：新增了attendance_information_tabel.py文件，该文件有AttendanceRecord和AttendanceManager两个类。
  AttendanceManager中有添加考勤记录的方法、查询某个考勤记录学生是否签到的方法、查看该表的所有数据的方法。

#### 改进

- [改进1]：修改了todo.md文件。
- [改进2]：将docs文件放在来8080端口展示，可以通过浏览器访问。
- [改进3]：重构了app.py文件，将其改成了一个flask的web应用。

#### 修复

无

### 版本 0.6.0 (2023.12.19)

```angular2html
@Author : Jin Yang / zixian Zhu
@Date   : 2023/12/19
@Submit_branch: version_1
```

#### 新特性

- [功能1]：新增了clss_schedule_table.py文件，该文件有ClassScheduleRecord和ClassScheduleManager两个类。
- [功能2]：完成了学生课程表API、学生登录API、老师登录API，具体详情看线上文档。

#### 改进

- [改进1]：修改了course表结构，详情请看文档。
- [改进2]：新增了class_schedule表，用于记录课程的上课时间。详情请看文档。
- [改进3]：将models里面的course_tabel.py文件进行了拓展，使得其符合新的表结构。

#### 修复

- [修复1]：修复了wx-app课程表页面展示的bug。

### 版本 0.7.0 (2023.12.29)

```angular2html
@Author : qicao Dai/ shangming Chen / zixian Zhu
@Date   : 2023/12/29
@Submit_branch: version_1
```

#### 新特性

- [功能1]：完成了老师缺勤名单API、请假条API具体详情看线上文档。

#### 改进

- 无

#### 修复

- 无

### 版本 0.8.0 (2023.12.31)

```angular2html
@Author : zixian Zhu
@Date   : 2023/12/31
@Submit_branch: version_1
```

#### 新特性

- [功能1]：完成了老师发布考勤API、老师详情信息API、学校详情信息API，具体详情看线上文档。
- [功能2]：新建了一个post_attendance_table.py文件，该文件有PostAttendanceRecord和PostAttendanceManager两个类。用于老师发布考勤的相关操作。

#### 改进

- [改进1]：新增了post_attendance_information表，详情请看腾讯文档。
- [改进2]：修改了Student_information的部分方法的返回值，并且删除了三个属性列。

#### 修复

- 无

### 版本 0.9.0 (2024.1.2)

```angular2html
@Author : qicao Dai/ jin Yang
@Date   : 2024/1/2
@Submit_branch: version_1
```

#### 新特性

- [功能1]：完成了学生考勤API、获取请假审批API开发具体详情看线上文档。

#### 改进

- 无

#### 修复

- 无
  
### 版本 0.10.0 (2024.1.3)
  

```angular2html
@Author : shangming Chen/ zixian Zhu
@Date   : 2024/1/3
@Submit_branch: version_1
```

#### 新特性

- 无更新更新功能，将原来version_1.1分支合并到了version_1分支。功能没有改变

#### 改进

- 修改了学生发出请假请求API的method，将其改成了post方法。

#### 修复

- 无

### 版本 0.11.0 (2024.1.3)

```angular2html
@Author : zixian Zhu
@Date   : 2024/1/3
@Submit_branch: version_1
```

#### 新特性

- teacher_routes新增老师审核请假API，具体详情看线上文档。

#### 改进

- 修改了学生考勤API接受的参数和其内部代码逻辑。
- 修改了学生请假API接受的参数和其内部代码逻辑。
- 修改post_attendance_information表的结构，使得每个code唯一。
- 修改了attendance_information表的结构，新增一个reason列。
- 修改了clss_schedule表的结构，每周每种课程只能上一次。

#### 修复

- 修复了teacher_routes里面测试单元post_attendance单元的bug。
- 修复了student_routse里面测试单元absence_on_leave单元的bug。
- 修复了student_routse里面测试单元punch_in单元的bug。

### 版本 1.0.0 (2024.7.2)

```angular2html
@Author : zixian Zhu
@Date   : 2024/7/2
@Submit_branch: version_1
```

#### 更新内容
1. 对项目进行了一次大重构。使得功能重新恢复正常
2. 优化了文档内容，配备了详细的部署步骤。
3. 新增了测试文件，用于检测各个路由是否完整
4. 新增了项目依赖文件，可以一键配置该项目的虚拟环境
5. 新增了SQL文件夹，可以一键导入数据库管理软件完成数据库的初始化

#### 修复
- 修复了student_routse中无法正常登陆的bug。