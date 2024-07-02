<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-02 00:12:48
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 10:51:37
 * @FilePath: /Student Attendance System/docs/API/请假条API.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-02 00:12:48
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 10:44:56
 * @FilePath: /Student Attendance System/docs/API/请假条API.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 学生请假API

```
接口名称: "学生发出请假请求API"
开发负责人: 陈尚铭
完成日期: 2023-12-29
```

## **已完成**✅

## 概述

该接口实现了学生通过输入学号、课程号、老师工号、课次来现创建对考勤数据库添加请假纪律。

## 基本信息

Base URL: `http://127.0.0.1:5000`

## 发出请假请求

- Method: `POST`
- header: `{ 'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'}`
- route: `/student_manager/absence_on_leave`
- Param:
  - *student_id(String):学生的唯一标识
  - *course_id(String):课程的唯一标识
  - *course_number(Int):课次，在3-18之间
  - *reason(String)：请假理由

## 响应

- 成功状态：200
- 失败状态1：410（课程号输入错误）
- 失败状态3：412（课次输入有误，超出范围）
- 失败状态4：420（考勤记录已存在，重复申请）
- 失败状态5：400（请求header错误）
- 失败状态5：500（非法请求）

## 示例代码

```Javascript
  your_fuction_name(){
  // 请求的接口地址
  var apiUrl = 'http://127.0.0.1:5000/student_manager/absence_on_leave';
  wx.request({
      url: apiUrl,
      method: 'GET',
      header: {
        'app': 'wx-app'
      },
      data:{
        'student_id': '2021611001',
        'course_id': 'c1',
        'teacher_id': 'T001',
        'course_number': '10'
      },
      success: function (res) {
          if (res.statusCode === 200) {
              // 接受参数
              var result = res.data;
              console.log(result.msg)
          } else {
              // 捕捉状态报错
              console.error('Error:', res.statusCode, res.data);
          }
      },
      fail: function (error) {
          // 捕捉请求报错
          console.error('Request failed:', error);
      }
  });
}
```