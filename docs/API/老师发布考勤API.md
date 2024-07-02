# 老师发布考勤API
```
接口名称: "老师发布考勤API"
开发负责人: 祝子贤
完成日期: 2023-12-31
```

## **已完成**✅

## 概述

老师发布考勤

## 基本信息

Base URL: `http://127.0.0.1:5000`

## 老师发布考勤信息

- Method: `POST`
- header: `{ 'app': 'wx-app', 'Content-Type': 'application/x-www-form-urlencoded'}`
- route: `/teacher_manager/post_attendance`
- Param: 
  - *course_name (String): 课程名称
  - *course_id (String)：课程号
  - *course_no (Int)：课程周次
  - *attendance_start_time (Date)：考勤开始时间
  - *attendance_end_time (Date)：考勤结束时间
  - *code (String)：签到码

## 响应

- 成功状态：200
- 失败状态1：500（请求非法，可能是路径错误）
- 失败状态2：502（服务器未开启）
- 失败状态3：400（请求header错误）

## 示例代码

```Javascript
  your_function_name() {
    // 创建一个新的Date对象，它将包含当前的日期和时间
    var currentTime = new Date();

    // 计算后一天的时间
    var nextDay = new Date(currentTime);
    nextDay.setDate(currentTime.getDate() + 1);

    // 获取年、月、日、时、分、秒
    var currentTimeYear = currentTime.getFullYear();
    var currentTimeMonth = currentTime.getMonth() + 1; // 月份是从0开始的，所以要加1
    var currentTimeDay = currentTime.getDate();
    var currentTimeHours = currentTime.getHours();
    var currentTimeMinutes = currentTime.getMinutes();
    var currentTimeSeconds = currentTime.getSeconds();
    var nextDayYear = nextDay.getFullYear();
    var nextDayMonth = nextDay.getMonth() + 1; // 月份是从0开始的，所以要加1
    var nextDayDay = nextDay.getDate();
    var nextDayHours = nextDay.getHours();
    var nextDayMinutes = nextDay.getMinutes();
    var nextDaySeconds = nextDay.getSeconds();

    // 格式化成字符串
    var formattedTime = currentTimeYear + '-' + currentTimeMonth + '-' + currentTimeDay + ' ' + currentTimeHours + ':' + currentTimeMinutes + ':' + currentTimeSeconds;
    var formattedNextDay = nextDayYear + '-' + nextDayMonth + '-' + nextDayDay + ' ' + nextDayHours + ':' + nextDayMinutes + ':' + nextDaySeconds;

    // 请求的接口地址
    var apiUrl = 'http://127.0.0.1:5000/teacher_manager/post_attendance';
    wx.request({
      url: apiUrl,
      method: 'POST',
      header: {
        'app': 'wx-app',
        'Content-Type': 'application/x-www-form-urlencoded', // 设置请求头,表示请求体的内容将以 URL 编码形式传输
      },
      data: {
        'course_name': '操作系统原理',
        'course_id': 'c1',
        'course_no': 16,
        'attendance_start_time': formattedTime,
        'attendance_end_time': formattedNextDay,
        'code': 'c0003'
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
