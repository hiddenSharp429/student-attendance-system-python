<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-02 00:12:48
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 10:51:33
 * @FilePath: /Student Attendance System/docs/API/学生考勤API.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<!--
 * @Author: hiddenSharp429 z404878860@163.com
 * @Date: 2024-07-02 00:12:48
 * @LastEditors: hiddenSharp429 z404878860@163.com
 * @LastEditTime: 2024-07-02 10:45:12
 * @FilePath: /Student Attendance System/docs/API/学生考勤API.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 学生考勤API
```
接口名称: "punch_in"
开发负责人: 杨锦
完成日期: 2024.01.01
```

## **已完成**✅

## 概述

该API接口提供给学生使用；学生通过该接口实现打卡签到老师发布的考勤任务。

## 基本信息

Base URL: `http://127.0.0.1:5000`

## 获取学生课程表

- Method: `POST`
- header: `{ 'app': 'wx-app'}, 'Content-Type': 'application/x-www-form-urlencoded'`
- route: `/student_manager/punch_in`
- Param:
    - *student_id(String): 学生的唯一标识符
    - *punch_in_time(String): 学生打卡签到时间
    - *code(String): 考勤任务的签到码


## 响应

- 成功状态1：200（考勤打卡成功）
- 成功状态2：201（添加缺勤记录）
- 失败状态1：500（请求非法，可能是路径错误）
- 失败状态2：502（服务器未开启）
- 失败状态3：400（请求header错误）
- 失败状态4：404（请求的数据错误）

## 示例代码

```Javascript
api_test(){
  // 请求的接口地址
  var apiUrl = 'http://127.0.0.1:5000/student_manager/punch_in';
  wx.request({
      url: apiUrl,
      method: 'GET',
      header: {
        'app': 'wx-app'
      },
      data:{
        'student_id':'2021611012',
        'punch_in_time':'2024-01-01 09:20:34',
        'code':'c0003'
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