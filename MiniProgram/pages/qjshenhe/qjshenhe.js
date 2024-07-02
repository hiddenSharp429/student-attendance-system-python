var app = getApp()
Page({
  data: {
    leaveApplications: []
  },

  onLoad: function () {
    app.editTabBar1();    //显示自定义的底部导航
    this.getLeaveApplications();
  },

  getLeaveApplications: function () {
    var that = this;
    var apiUrl = 'http://43.136.80.11:5000/teacher_manager/get_leave_requests';
    wx.request({
      url: apiUrl,
      header: {
       'app': 'wx-app'
      },
      data: {
       'teacher_id': 'T001',
     },
      method: 'GET',
      success: function (res) {
        that.setData({
          leaveApplications: res.data.leave_requests
        });
        console.log('获取请假申请列表成功',that.data.leaveApplications);
      },
      fail: function (err) {
        console.error('获取请假申请列表失败', err);
      }
    });
  },

  approveLeave: function (e) {
       var that = this; 
    var index = e.currentTarget.dataset.index;
    var application = this.data.leaveApplications[index];
    var student_id = application.studentId;
    var course_id = application.courseCode;
    var course_no = application.courseWeek;
    console.log('通过请假申请：', this.data.leaveApplications[index]);
    var apiUrl = 'http://43.136.80.11:5000/teacher_manager/review_leave_request';
    wx.request({
      url: apiUrl,
      method: 'POST',
      header: {
        'app': 'wx-app',
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
       'student_id': student_id,
       'course_id': course_id,
       'course_no': course_no,
       'is_reviewed': true
      },
      success: function (res) {
        console.log('通过申请成功', res);
        wx.showToast({
              title: '通过申请成功',
              icon: 'none'
            });
        that.getLeaveApplications();
      },
      fail: function (err) {
        console.error('通过申请失败', err);
        wx.showToast({
              title: '通过申请失败',
              icon: 'none'
            });
      }
    });
  },

  rejectLeave: function (e) {
       var that = this; 
       var index = e.currentTarget.dataset.index;
       var application = this.data.leaveApplications[index];
       var student_id = application.studentId;
       var course_id = application.courseCode;
       var course_no = application.courseWeek;

    console.log('拒绝请假申请：', this.data.leaveApplications[index]);
    var apiUrl = 'http://43.136.80.11:5000/teacher_manager/review_leave_request';
    wx.request({
      url: apiUrl,
      method: 'POST',
      header: {
        'app': 'wx-app',
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
       'student_id': student_id,
        'course_id': course_id,
        'course_no': course_no,
        is_reviewed: false
      },
      success: function (res) {
        console.log('拒绝申请成功', res);
        wx.showToast({
              title: '拒绝申请成功',
              icon: 'none'
            });
        that.getLeaveApplications();
      },
      fail: function (err) {
        console.error('拒绝申请失败', err);
        wx.showToast({
              title: '拒绝申请失败',
              icon: 'none'
            });
      }
    });
  },
});