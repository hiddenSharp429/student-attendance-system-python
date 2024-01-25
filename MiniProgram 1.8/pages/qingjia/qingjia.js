// pages/qingjia/qingjia.js
var app = getApp()
Page({

       /**
        * 页面的初始数据
        */
       data: {
              week: ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
              weekIndex: 0,
              stuId: '',
              courseData: [], // 原始从服务器获取的课程数据
              courseNames: [], // 存储课程名称的数组
              selectedCourse: '', // 当前选中的课程名称
              // 初始化页面数据
              contactInfo: '',
              expOverview: '',
       },
       weekchoose(e) {
              this.setData({
                     weekIndex: e.detail.value
              });
       },
       classchoose(e) {
              // 更新选中的课程名称
              this.setData({
                     selectedCourse: this.data.courseNames[e.detail.value]
              });
       },
       // 处理文本域输入
       handleTextAreaInput: function (e) {
              this.setData({
                     expOverview: e.detail.value // 将输入的值设置到expOverview
                     
              });
              console.log(this.data.expOverview)
       },
       /**
        * 生命周期函数--监听页面加载
        */
       onLoad: function () {
              app.editTabBar(); // 显示自定义的底部导航
              const that = this; // 在回调函数之外保存对页面this的引用
              // 获得缓存的用户ID的课程
              wx.getStorage({
                     key: 'stuId',
                     success: function (res) {
                            console.log(res.data);
                            that.setData({
                                   stuId: res.data
                            });
                            console.log(that.data.stuId);
                            that.get_stu_class(that.data.stuId);
                     }
              });


       },
       //获得课程信息
       get_stu_class(stuId) {
              var that = this; // 保存当前页面的this引用
              // 请求的接口地址
              var apiUrl = 'http://43.136.80.11:5000/student_manager/view_student_courses';
              console.log(stuId)
              wx.request({
                     url: apiUrl,
                     method: 'GET',
                     header: {
                            'app': 'wx-app'
                     },
                     data: {
                            'student_id': stuId,
                            'semester': '2023',
                            'week_no': 5
                     },
                     success: function (res) {
                            if (res.statusCode === 200) {
                                   // 接受参数
                                   var result = res.data;
                                   //      console.log(result.class_schedule_records)
                                   that.setData({
                                          courseData: result.class_schedule_records,
                                   }, () => {
                                          that.fetchCourseData();
                                   });
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
       },
       //将课程信息保存起来
       fetchCourseData: function () {
              var that = this;
              var names = that.data.courseData.map(function (course) {
                     return course.course_name;
              });
              // 去除重复的课程名称
              var uniqueNames = [...new Set(names)];
              that.setData({
                     courseNames: uniqueNames,
                     selectedCourse: uniqueNames[0] || '' // 设置默认值，如果数组为空则为空字符串

              });
              console.log(that.data.courseNames)
       },

       // 提交表单时调用的函数
       submitForm: function (e) {
              var apiUrl = 'http://43.136.80.11:5000/student_manager/absence_on_leave';

              const formData = e.detail.value;

              // 构造请求数据
              const requestData = {
                     // student_id: this.data.stuId, // 示例学号
                     // course_id:'c1', // 用户选择的课程ID
                     // course_number: 'T001', // 用户选择的周次
                     // reason: this.data.expOverview, // 用户输入的请假理由
                     'student_id': '2021611001',
        'course_id': 'c1',
        'teacher_id': 'T001',
        'course_number': '10'

              };


              // 发送请求
              wx.request({
                     url: apiUrl,
                     method: 'POST',
                     header: {
                            'app': 'wx-app',
                            'Content-Type': 'application/x-www-form-urlencoded'
                     },
                     data: requestData,
                     success: function (res) {
                            switch (res.statusCode) {
                                   case 200:
                                          wx.showToast({
                                                 title: '提交成功',
                                                 icon: 'success',
                                                 duration: 2000
                                          });
                                          break;
                                   case 410:
                                          wx.showToast({
                                                 title: '课程号输入错误',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                                   case 412:
                                          wx.showToast({
                                                 title: '课次输入有误',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                                   case 420:
                                          wx.showToast({
                                                 title: '重复申请',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                                   case 400:
                                          wx.showToast({
                                                 title: '请求头错误',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                                   case 500:
                                          wx.showToast({
                                                 title: '非法请求',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                                   default:
                                          wx.showToast({
                                                 title: '未知错误',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                            }
                     },
                     fail: function (error) {
                            wx.showToast({
                                   title: '请求失败',
                                   icon: 'none',
                                   duration: 2000
                            });
                     }
              });
       },
       /**
        * 生命周期函数--监听页面初次渲染完成
        */
       onReady() {

       },

       /**
        * 生命周期函数--监听页面显示
        */
       onShow() {

       },

       /**
        * 生命周期函数--监听页面隐藏
        */
       onHide() {

       },

       /**
        * 生命周期函数--监听页面卸载
        */
       onUnload() {

       },

       /**
        * 页面相关事件处理函数--监听用户下拉动作
        */
       onPullDownRefresh() {

       },

       /**
        * 页面上拉触底事件的处理函数
        */
       onReachBottom() {

       },

       /**
        * 用户点击右上角分享
        */
       onShareAppMessage() {

       }
})