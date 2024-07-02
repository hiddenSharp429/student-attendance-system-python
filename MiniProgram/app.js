//app.js

App({
  globalData: {
    windowWidth: '',
    windowHeight: '',
    screenHeight: '',
    worknavid: '',
    qk:'LZBBZ-PQQCF-SNQJI-JSYKC-YR3IK-BBF26',
    //个人中心显示登录人信息
    who:'',
    id:'',
    name:'',
    tea_phone_number: '',
    stu_phone_number:'',
    avatarUrl: "",
    //课程表
    selectedWeek: 1, // 默认选择第1周
    selectedSemester: "2022-2023-1" // 默认选择2022-2023学年第1学期
  },
  onLaunch: function () {
    this.globalData.tea_phone_number = '12345678901';
    this.globalData.stu_phone_number = '12345678901';

    var that = this;
    wx.getSystemInfo({
      success: function (res) {
        that.globalData.windowWidth = res.windowWidth;
        that.globalData.windowHeight = res.windowHeight;
        that.globalData.screenHeight = res.screenHeight
      },
    })
  },

  //第一种底部  
       editTabBar: function () {
         //使用getCurrentPages可以获取当前加载中所有的页面对象的一个数组，数组最后一个就是当前页面。
      
         var curPageArr = getCurrentPages();    //获取加载的页面
         var curPage = curPageArr[curPageArr.length - 1];    //获取当前页面的对象
         var pagePath = curPage.route;    //当前页面url
         if (pagePath.indexOf('/') != 0) {
           pagePath = '/' + pagePath;
         }
         
         var tabBar = this.globalData.tabBar;
         for (var i = 0; i < tabBar.list.length; i++) {
           tabBar.list[i].active = false;
           if (tabBar.list[i].pagePath == pagePath) {
             tabBar.list[i].active = true;    //根据页面地址设置当前页面状态    
           }
         }
         curPage.setData({
           tabBar: tabBar
         });
       },
       //第二种底部，原理同上
       editTabBar1: function () {
         var curPageArr = getCurrentPages();
         var curPage = curPageArr[curPageArr.length - 1];
         var pagePath = curPage.route;
         if (pagePath.indexOf('/') != 0) {
           pagePath = '/' + pagePath;
         }
         var tabBar = this.globalData.tabBar1;
         for (var i = 0; i < tabBar.list.length; i++) {
           tabBar.list[i].active = false;
           if (tabBar.list[i].pagePath == pagePath) {
             tabBar.list[i].active = true; 
           }
         }
         curPage.setData({
           tabBar: tabBar
         });
       },
       globalData: {
         //学生底部导航栏显示
         tabBar: {
           "color": "#9E9E9E",
           "selectedColor": "#f00",
           "backgroundColor": "#fff",
           "borderStyle": "#ccc",
           "list": [     
             {
              "pagePath": "/pages/kechengbiao/kechengbiao",
              "text": "课程表",
             "iconPath": "/pages/img/member.png",
             "selectedIconPath": "/pages/img/member.png",
              "selectedColor": "#4EDF80",
               "clas": "menu-item",
               active: false
            },
            {
              "pagePath": "/pages/qiandao/qiandao",
              "text": "签到",
              "iconPath": "/pages/img/member.png",
              "selectedIconPath": "/pages/img/member.png",
              "selectedColor": "#4EDF80",
               "clas": "menu-item",
               active: false
            },
            {
             "pagePath": "/pages/qingjia/qingjia",
             "text": "请假",
             "iconPath": "/pages/img/member.png",
             "selectedIconPath": "/pages/img/member.png",
             "selectedColor": "#4EDF80",
               "clas": "menu-item",
               active: false
           },
            {
              "pagePath": "/pages/stuperson/stuperson",
              "text": "个人中心",
              "iconPath": "/pages/img/member.png",
              "selectedIconPath": "/pages/img/member.png",
              "selectedColor": "#4EDF80",
               "clas": "menu-item",
               active: false
            }
           ],
           "position": "bottom"
         },
         //老师底部导航栏显示
         tabBar1: {
           "color": "#9E9E9E",
           "selectedColor": "#f00",
           "backgroundColor": "#fff",
           "borderStyle": "#ccc",
           "list": [
              {
                     "pagePath": "/pages/qjshenhe/qjshenhe",
                     "text": "请假审批",
                     "iconPath": "/pages/img/member.png",
                     "selectedIconPath": "/pages/img/member.png",
                     "selectedColor": "#4EDF80",
                      "clas": "menu-item",
                      active: false
                   },
                   {
                     "pagePath": "/pages/fabukq/fabukq",
                     "text": "发布",
                     "iconPath": "/pages/img/member.png",
                     "selectedIconPath": "/pages/img/member.png",
                     "selectedColor": "#4EDF80",
                      "clas": "menu-item",
                      active: false
                   },
                   {
                    "pagePath": "/pages/kqtongji/kqtongji",
                    "text": "统计",
                    "iconPath": "/pages/img/member.png",
                    "selectedIconPath": "/pages/img/member.png",
                    "selectedColor": "#4EDF80",
                      "clas": "menu-item",
                      active: false
                  },
                   {
                     "pagePath": "/pages/person/person",
                     "text": "个人中心",
                     "iconPath": "/pages/img/member.png",
                     "selectedIconPath": "/pages/img/member.png",
                     "selectedColor": "#4EDF80",
                      "clas": "menu-item",
                      active: false
                   }
           ],
           "position": "bottom"
         }
       }
})
