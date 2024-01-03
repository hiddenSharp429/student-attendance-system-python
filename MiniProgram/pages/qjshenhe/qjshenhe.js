var app = getApp()
Page({
  data: {
    leaveApplications: [
      {
        name: '小明',
        reason: '生病请假'
      },
      {
        name: '小红',
        reason: '家里有事请假'
      },
      {
        name: '小刚',
        reason: '参加比赛请假'
      }
    ]
  },
  onLoad:function(){
    app.editTabBar1();    //显示自定义的底部导航
    this.get_application();
  },
  //测试接口
  get_application(){
              // 请求的接口地址
              var apiUrl = 'http://43.136.80.11:5000/teacher_manager/get_leave_requests';
              wx.request({
                url: apiUrl,
                method: 'GET',
                header: {
                  'app': 'wx-app'
                },
                data: {
                  'teacher_id': 'T001',
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
            
  },
  approveLeave: function(e) {
    var index = e.currentTarget.dataset.index;
    console.log('通过请假申请：', this.data.leaveApplications[index]);
    
    // 通过请假申请的逻辑处理代码...
  },

  rejectLeave: function(e) {
    var index = e.currentTarget.dataset.index;
    console.log('拒绝请假申请：', this.data.leaveApplications[index]);
    
    // 拒绝请假申请的逻辑处理代码...
  }
});