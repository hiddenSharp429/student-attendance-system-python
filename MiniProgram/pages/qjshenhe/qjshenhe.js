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