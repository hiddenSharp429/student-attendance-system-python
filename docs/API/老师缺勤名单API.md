<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-02 00:12:48
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 10:51:40
 * @FilePath: /Student Attendance System/docs/API/老师缺勤名单API.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 老师缺勤名单API

```
接口名称: "老师缺勤名单API"
开发负责人: 代青草
完成日期: 2023-12-29
```

## **已完成**✅

## 概述

该接口实现老师缺勤名单API。

## 基本信息

Base URL: `http://127.0.0.1:5000`

## 发出请假请求

- Method: `GET`
- header: `{ 'app': 'wx-app'}`
- route: `/teacher_manager/view_absentee_list`
- Param:
    - *course_no(Int):课程的周次
    - *course_id(String):课程的唯一标识

## 响应

- 成功状态：200
- 失败状态5：400（请求header错误）
- 失败状态5：500（非法请求）

## 示例代码

```Javascript
  your_fuction_name(){
  // 请求的接口地址
  var apiUrl = 'http://127.0.0.1:5000/teacher_manager/view_absentee_list';
  wx.request({
      url: apiUrl,
      method: 'GET',
      header: {
        'app': 'wx-app'
      },
      data:{
        'student_id': '2',
        'course_id': 'c1',
      },
      success: function (res) {
          if (res.statusCode === 200) {
            // 接受参数
              var result = res.data;
              console.log(result.absent_students)
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