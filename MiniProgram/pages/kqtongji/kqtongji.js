var app = getApp()
Page({

  data: {
    tabBar: {}, // 确保你的data里有tabBar对象
    radioValue: '1', // 默认选中缺勤名单
    courseNos: ['操作系统原理', '编译原理', '软件工程', 'ELC4'],
    courseIds: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    selectedWeek: '请选择课程',
    selectedCourse: '请选择周次',
    qingjiaList: [], // 缺勤学生列表
    absenceList: [] // 请假学生列表
  },

  onLoad: function () {
    app.editTabBar1(); // 显示自定义的底部导航
    // 初始化radioValue
    this.setData({
      radioValue: '1'
    });
  },

  onCourseNoChange: function (e) {
    this.setData({
      selectedWeek: this.data.courseNos[e.detail.value]
    });
  },

  onCourseIdChange: function (e) {
    this.setData({
      selectedCourse: this.data.courseIds[e.detail.value]
    });
  },

  onRadioChange: function (e) {
    this.setData({
      radioValue: e.detail.value
    });
  },

  fetchAbsenceList: function () {
    const { selectedWeek, selectedCourse } = this.data;
    if (selectedWeek === '请选择课程' || selectedCourse === '请选择周次') {
      wx.showToast({
        title: '请选择课程和周次',
        icon: 'none'
      });
      return;
    }
    // 模拟数据更新，实际应从服务器获取
    this.setData({
      qingjiaList: ["梁根华", "陆伟"], // 缺勤学生列表
      absenceList: ["代青草", "吴茵"] // 请假学生列表
    });
  }
});