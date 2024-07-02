var app = getApp();

Page({
       data: {
              courseName: '',
              courseCode: '',
              courseWeek: '',
              signInCode: '',
              date: '',
              startTime: '',
              endTime: ''
       },

       onLoad: function () {
              app.editTabBar1(); //显示自定义的底部导航
       },
       inputCourseName: function (e) {
              this.setData({
                     courseName: e.detail.value
              });
       },

       inputCourseCode: function (e) {
              this.setData({
                     courseCode: e.detail.value
              });
       },

       inputCourseWeek: function (e) {
              this.setData({
                     courseWeek: e.detail.value
              });
       },

       inputSignInCode: function (e) {
              this.setData({
                     signInCode: e.detail.value
              });
       },

       selectDate: function (e) {
              this.setData({
                     date: e.detail.value
              });
       },
       selectStartTime: function (e) {
              this.setData({
                     startTime: e.detail.value
              });
       },
       selectEndTime: function (e) {
              this.setData({
                     endTime: e.detail.value
              });
       },

       submitAttendance: function () {
              console.log('课程名称：', this.data.courseName);
              console.log('课程号：', this.data.courseCode);
              console.log('课程周次：', this.data.courseWeek);
              console.log('签到码：', this.data.signInCode);
              console.log('考勤日期：', this.data.date);
              console.log('考勤开始时间：', this.data.startTime);
              console.log('考勤结束时间：', this.data.endTime);
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


              var apiUrl = 'http://43.136.80.11:5000/teacher_manager/post_attendance';
              wx.request({
                     url: apiUrl,
                     method: 'POST',
                     header: {
                            'app': 'wx-app',
                            'Content-Type': 'application/x-www-form-urlencoded'
                     },
                     data: {
                            course_name: this.data.courseName,
                            course_id: this.data.courseCode,
                            course_no: parseInt(this.data.courseWeek),
                            attendance_start_time: formattedTime,
                            attendance_end_time: formattedNextDay,
                            code: this.data.signInCode
                     },
                     success: function (res) {
                            console.log('考勤发布成功', res);
                            wx.showToast({
                              title: '发布考勤成功',
                            })
                            // 处理成功响应的逻辑
                     },
                     fail: function (error) {
                            console.log('考勤发布失败', error);
                            wx.showToast({
                                   title: '发布考勤失败',
                                 })
                            // 处理失败响应的逻辑
                     }
              });
       }
});