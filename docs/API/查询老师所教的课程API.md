<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-02 00:12:48
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 10:51:47
 * @FilePath: /Student Attendance System/docs/API/查询老师所教的课程API.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 查询老师所教的课程API
```
接口名称: "查询老师所选的课程API"
开发负责人: 陈尚铭
完成日期: 2024-01-01
```

## **已完成**✅

## 概述

该接口实现了老师可以查询到自己需要教授哪些课

## 基本信息

Base URL: `http://127.0.0.1:5000`

## 获取学生课程表

- Method: `GET`
- header: `{ 'app': 'wx-app'}`
- route: `/teacher_manager/search_teacher_course`
- Param:
  *student_id(String):老师的唯一标识

## 响应

- 成功状态：200
- 失败状态1：500（请求非法，可能是路径错误）
- 失败状态3：400（请求header错误）

## 示例代码

```Javascript
  your_fuction_name(){
  // 请求的接口地址
  var apiUrl = 'http://127.0.0.1:5000/teacher_manager/search_teacher_course';
  wx.request({
      url: apiUrl,
      method: 'GET',
      header: {
        'app': 'wx-app'
      },
      data:{
        'student_id': 'T001',
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