# 获取单个学生API
```
接口名称: "获取单个学生API"
开发负责人: 祝子贤
完成日期: "2023-12-31"
```

## **已完成**✅


## 概述
该 API 提供了对单个学生信息获取功能。通过该 API，您可以获取单个学生的信息。

## 基本信息
Base URL: `http://127.0.0.1:5000`


## 获取学生课程表
- Method: `GET`
- route: `/student_manager/view_signal_student`
- Param:
    - *student_id (String): 学生的唯一标识符。

## 响应
- 成功状态：200
- 失败状态1：500（请求非法，可能是路径错误）
- 失败状态2：502（服务器未开启）
- 失败状态3：400（请求header错误）

## 示例代码
```Javascript
  your_fuction_name() {
    // 请求的接口地址
    var apiUrl = 'http://127.0.0.1:5000/student_manager/view_signal_student';
    wx.request({
      url: apiUrl,
      method: 'GET',
      header: {
        'app': 'wx-app'
      },
      data: {
        'student_id': '2021611001',
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
