// pages/login/index.js
import {
       M
} from '../../utils/M.js';
const m = new M();
let app = getApp();
let that;
Page({

       /**S
        * 页面的初始数据
        */
       data: {
              role: ['学生', '教师'],
              roleIndex: 0
       },
       role(e) {
              that.setData({
                     roleIndex: e.detail.value
              });
       },
       /**
        * 生命周期函数--监听页面加载
        */
       onLoad: function (options) {
              that = this;
              that.setData({
                     width: app.globalData.windowWidth,
                     height: app.globalData.windowHeight
              });
       },

       /**
        * 生命周期函数--监听页面显示
        */
       onShow: function () {
              let loginStatus = wx.getStorageSync('s');
              if (loginStatus) {
                     wx.reLaunch({
                            url: '../index/index',
                     });
                     return;
              }
       },
       login(e) {
              if (e.detail.value.userName == "") {
                     m.showTost('请输入学号');
                     return;
              } else if (e.detail.value.userPwd == "") {
                     m.showTost('请输入姓名');
                     return;
              } else {
                     // m.showLoading('正在登录');
                     if (e.detail.value.role == 0) {
                            //测试代码
                            // console.log(typeof(e.detail.value.userName))
                            // console.log(typeof(e.detail.value.userPwd)) 
                            m.student_signup(
                                   e.detail.value.userName,
                                   e.detail.value.userPwd
                            )
                     } else if (e.detail.value.role == 1) { //测试
                            m.teacher_signup(
                                   e.detail.value.userName,
                                   e.detail.value.userPwd
                            )
                     }
              }
       },
       get_account: function (event) {

              const usrname = event.detail.value
              this.setData({
                     usrname: usrname
              })
              app.globalData.name = usrname

       },

       get_password: function (event) {

              const usrid = event.detail.value
              this.setData({
                     usrid: usrid
              })
              app.globalData.id = usrid

       },
})