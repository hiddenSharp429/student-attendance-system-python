# 全部学生信息API

```
接口名称: "全部学生信息API"
开发负责人: 祝子贤
完成日期: "2023-12-6"
```
## **已完成**✅

## 概述
该 API 提供了对全部学生信息的查询功能。通过该 API，您可以获取全部学生信息。

## 基本信息
Base URL: `http://127.0.0.1:5000`

## 获取全部学生信息API
- Method: `GET`
- header: `{ 'app': 'wx-app'}`
- route: `/student_manager/view_all_students`
- Param: none

## 响应
- 成功状态：200
- 失败状态1：500（请求非法，可能是路径错误）
- 失败状态2：502（服务器未开启）
- 失败状态3：400（请求header错误）

## 示例代码
```Javascript
  your_function_name(){
    // 请求的接口地址
    var url = 'http://127.0.0.1:5000/student_manager/view_all_students'; 
    wx.request({
        url: apiUrl,
        method: 'GET',
        header:{
          'app': 'wx-app',
        },
        success: function (res) {
            if (res.statusCode === 200) {
                // 接受请求成功所获取到的数据
                var result = res.data;
                ......
                ......
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