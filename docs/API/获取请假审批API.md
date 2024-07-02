<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-02 00:12:48
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 10:51:43
 * @FilePath: /Student Attendance System/docs/API/获取请假审批API.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 获取请假审批API
```
接口名称: "获取请假审批API"
开发负责人: 代青草
完成日期: 2024.1.2
```

## **已完成**✅

## 概述
通过这个接口可以返回某个老师所教全部课程的全部学生的请假信息。
返回的参数有:
- course_id：课程ID
- course_no：课程周次
- data：考勤的日期
- student_id：学生ID
- student_name：学生姓名


## 基本信息

Base URL: `http://127.0.0.1:5000`

## 获取请假审批

- Method: `GET`
- header: `{ 'app': 'wx-app'}`
- route: `/teacher_manager/get_leave_requests`
- Param:
  - *teacher_id (String): 老师的唯一标识符。

## 响应

- 成功状态：200
- 失败状态1：500（请求非法，可能是路径错误）
- 失败状态2：502（服务器未开启）
- 失败状态3：400（请求header错误）

## 示例代码

```Javascript
   your_fuction_name() {
    // 请求的接口地址
    var apiUrl = 'http://127.0.0.1:5000/teacher_manager/get_leave_requests';
    wx.request({
      url: apiUrl,
      method: 'GET',
      header: {
        'app': 'wx-app'
      },
      data: {
        'teacher_id': 'T001',
      },
      success: function (res) {
        if (res.statusCode === 200) {
          // 接受参数
          var result = res.data;
          console.log(result)
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