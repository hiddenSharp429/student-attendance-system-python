# 老师审核请假API

```
接口名称: "老师审核请假API"
开发负责人: 祝子贤
完成日期: "2024-1-3"
```
## **已完成**✅

## 概述
该 API 提供了对某个老师所教的课程的全部学生的请假信息进行审核的功能。通过该 API，您可以对学生请假申请进行审批。

## 基本信息
Base URL: `http://127.0.0.1:5000`

## 获取全部学生信息API
- Method: `POST`
- header: `{ 'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'}`
- route: `/teacher_manager/review_leave_request`
- Param:
  - *student_id (String): 学生号
  - *course_id (String)：课程号
  - *course_no (Int)：课程周次
  - *is_reviewed (Boolean)：是否通过审批

## 响应
- 成功状态：200
- 失败状态1：500（请求非法，可能是路径错误）
- 失败状态2：502（服务器未开启）
- 失败状态3：400（请求header错误）
- 失败状态4：401（修改失败）

## 示例代码
```Javascript
  your_fuction_name(){
    // 请求的接口地址
    var apiUrl = 'http://127.0.0.1:5000/teacher_manager/review_leave_request';
    wx.request({
        url: apiUrl,
        method: 'POST',
        header: {
          'app': 'wx-app',
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        data:{
           // 需要传入的参数
          'student_id':'2021611011',
          'course_id': 'c1',
          'course_no': 14,
          'is_reviewed': true
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