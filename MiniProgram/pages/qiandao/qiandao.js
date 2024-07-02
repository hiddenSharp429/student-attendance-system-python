var app = getApp()
Page({

       /**
        * 页面的初始数据
        */
       data: {
              stuID: '',
              qiandaotime: '',
              qiandaocode: ''
       },

       // 更新学生ID
       updatecode: function (e) {
              this.setData({
                     qiandaocode: e.detail.value
              });
              console.log(this.data.qiandaocode)
       },

       // 签到函数
       qiandao: function () {
              // 获取当前时间
              var now = new Date();
              var year = now.getFullYear();
              var month = now.getMonth() + 1;
              var day = now.getDate();
              var hour = now.getHours();
              var minute = now.getMinutes();
              var second = now.getSeconds();

              // 添加前导零
              month = month < 10 ? '0' + month : month;
              day = day < 10 ? '0' + day : day;
              hour = hour < 10 ? '0' + hour : hour;
              minute = minute < 10 ? '0' + minute : minute;
              second = second < 10 ? '0' + second : second;

              // 格式化时间
              var timeStr = year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second;

              // 设置签到时间
              this.setData({
                     qiandaotime: timeStr
              });
              console.log(this.data.qiandaotime)
              var apiUrl = 'http://43.136.80.11:5000/student_manager/punch_in';
              var that = this;
              wx.request({
                     url: apiUrl,
                     method: 'POST',
                     header: {
                            'app': 'wx-app',
                            'Content-Type': 'application/x-www-form-urlencoded'
                     },
                     data: {
                            'student_id': that.data.stuID,
                            'punch_in_time': that.data.qiandaotime,
                            'code': that.data.qiandaocode
                     },
                     success: function (res) {
                            switch (res.statusCode) {
                                   case 200:
                                          wx.showToast({
                                                 title: '签到成功',
                                                 icon: 'success',
                                                 duration: 2000
                                          });
                                          break;
                                   case 201:
                                          wx.showToast({
                                                 title: '添加缺勤记录',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                                   case 502:
                                          wx.showToast({
                                                 title: '服务器未开启',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                                   case 500:
                                          wx.showToast({
                                                 title: '你已错过签到时间',
                                                 icon: 'none',
                                                 duration: 2000
                                          });
                                          break;
                                   case 404:
                                          wx.showToast({
                                                 title: '签到码错误',
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
                            console.error('Request failed:', error);
                     }
              });
       },

       /**
        * 生命周期函数--监听页面加载
        */
       onLoad: function () {
              app.editTabBar(); //显示自定义的底部导航
              var that = this;
              // 获得缓存
              wx.getStorage({
                     key: 'stuId',
                     success: function (res) {
                            that.setData({
                                   stuID: res.data
                            });
                     }
              });
              that = this;
              that.setData({
                     width: app.globalData.windowWidth,
                     height:app.globalData.windowHeight});
       },

       // 其他生命周期函数...

});