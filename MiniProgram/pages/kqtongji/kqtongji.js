var app = getApp()
Page({
  data: {
    array: ['选项1', '选项2', '选项3'],
    selectedValue: 0,
    radioValue: '1', // Default selected radio button
    tableHeader1: ['姓名', '学号', '课程'],
    tableData1: [
      { name: 'student1', studentId: '001', course: 'lesson1' },
      { name: 'student2', studentId: '002', course: 'lesson2' },
      // 添加更多数据行
    ],
    tableHeader2: ['姓名', '学号', '课程', '签到时间'],
    tableData2: [
      { name: 'student3', studentId: '003', course: 'lesson1', signInTime: '2023-01-01 10:00:00' },
      { name: 'student4', studentId: '004', course: 'lesson2', signInTime: '2023-01-01 11:30:00' },
      // 添加更多数据行
    ],
    currentTableData: [], // Holds the currently displayed table data
    currentTableHeader: [], // Holds the currently displayed table header
    
  },

  onLoad: function () {
    // 初始化为表1的数据和表头
    this.setData({
      currentTableData: this.data.tableData1,
      currentTableHeader: this.data.tableHeader1,
    });
  },
  onShow:function(){
    app.editTabBar1();    //显示自定义的底部导航
  },
  navigateBack: function () {
    wx.navigateBack({
      delta: 1,
    });
  },

  onInput: function (e) {
    console.log('输入内容：', e.detail.value);
  },

  onPickerChange: function (e) {
    console.log('选中的下拉列表项索引：', e.detail.value);
    this.setData({
      selectedValue: e.detail.value,
    });
  },

  onRadioChange: function (e) {
    console.log('选中的单选框值：', e.detail.value);
    this.setData({
      radioValue: e.detail.value,
    });

    // 根据选择的单选框切换表头和表格数据
    if (e.detail.value === '1') {
      this.setData({
        currentTableData: this.data.tableData1,
        currentTableHeader: this.data.tableHeader1,
      });
    } else if (e.detail.value === '2') {
      this.setData({
        currentTableData: this.data.tableData2,
        currentTableHeader: this.data.tableHeader2,
      });
    }
  }
  
});
