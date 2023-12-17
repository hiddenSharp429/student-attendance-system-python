Page({
  data: {
    title: '',
    date: '',
    startTime: '',
    endTime: ''
  },

  inputTitle: function(e) {
    this.setData({
      title: e.detail.value
    });
  },

  selectDate: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      date: e.detail.value
    });
  },

  inputLocation: function(e) {
    this.setData({
      location: e.detail.value
    });
  },

  selectStartTime: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      startTime: e.detail.value
    });
  },

  selectEndTime: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      endTime: e.detail.value
    });
  },

  submitAttendance: function() {
    console.log('考勤标题：', this.data.title);
    console.log('考勤日期：', this.data.date);
    console.log('考勤地点：', this.data.location);
    console.log('考勤开始时间：', this.data.startTime);
    console.log('考勤结束时间：', this.data.endTime);
    
    // 发布考勤的逻辑处理代码...
  }
});