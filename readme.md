# 版本更新

## 版本 0.1.0 (2023.11.27下午)
```angular2html
@Author : zixian Zhu
@Date   : 2023/11/27
@Submit_branch: version_1
```
### 新特性
- [功能1]：连接了远程服务器中的MySQL。
- [功能2]：student_information_table.py新增一个StudentManager类，用于学生表中的增删改查。

### 改进
- [改进1]：将读取本地的excel文件修改成了读取远程服务器上的数据库。
- [改进2]：完善了文件头和函数注释等细节。

### 修复
- [修复1]：修改原本的表名称student(student_information)。 
- [修复2]：修改了原本表student中的class属性列(class_no)，原因是class为保留关键字。

## 版本 0.2.0 (2023.11.27晚上)
```angular2html
@Author : zixian Zhu
@Date   : 2023/11/27
@Submit_branch: version_1
```
### 新特性
- [功能1]：teacher_information_table.py新增一个TeacherManager类，用于老师表中的增删改查。

### 改进
- [改进1]：修改了表的结构，具体详情请看文档。
- [改进2]：将各个表的测试数据都上传到了远程数据库中。

### 修复
无

## 版本 0.3.0 (2023.11.30晚上)
```angular2html
@Author : zixian Zhu
@Date   : 2023/11/30
@Submit_branch: version_1
```
### 新特性
- [功能1]：新增course_selection_table.py文件，该文件 
包含CourseSelectionRecord、CourseSelectionManager这两个类，用于学生选课表course_selection
中的查询操作
- [功能2]：新增了course.py文件，该文件包含Course、CourseManager两个类，用于课程表的中的相关操作
- [功能3]：每个表的Manager类都新增了对外提供的查询函数`execute_sql_query(self, sql_query)`
可以查询任意内容。
### 改进
- [改进1]：修改了course的表名称, course->course_seleciton
- [改进2]：新增了课程表course，用于记录课程的相关信息

### 修复
无

## 版本 0.4.0 (2023.12.6晚上)

```angular2html
@Author : zixian Zhu
@Date   : 2023/12/6
@Submit_branch: version_1
```

### 新特性

- [功能1]：删除原来的main.py，新增一个app.py，app.py中提供了一个简单的后端调用接口，用于获取所有学生信息。
- [功能2]：docs文件夹新增一个api调用的模板文档(api_template.md)和一个api交流文档(api.md)

### 改进

无

### 修复

无

## 版本 0.5.0 (2023.12.7)

```angular2html
@Author : zixian Zhu
@Date   : 2023/12/7
@Submit_branch: version_1
```

### 新特性

- [功能1]：新增了attendance_information_tabel.py文件，该文件有AttendanceRecord和AttendanceManager两个类。
AttendanceManager中有添加考勤记录的方法、查询某个考勤记录学生是否签到的方法、查看该表的所有数据的方法。

### 改进

- [改进1]：修改了todo.md文件

### 修复

无