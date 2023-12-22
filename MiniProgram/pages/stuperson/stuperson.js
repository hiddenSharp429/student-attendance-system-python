// pages/person/person.js
var app = getApp()
const defaultAvatarUrl = 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0';

Page({
  data: {
    isDisabled:true,  //表示页面加载完成时disabled为启用状态
    text:"修改信息",  //表示按钮初始文字为编辑
    inputFrame: "",
    lista: ["./1.jpg"],
    i: 0,

    userInfo: {
      avatarUrl: defaultAvatarUrl,
      nickName: '',
    },
    hasUserInfo: false,
    canIUseGetUserProfile: wx.canIUse('getUserProfile'),
    canIUseNicknameComp: wx.canIUse('input.type.nickname'),

   },
       onLoad:function(){
        app.editTabBar();    //显示自定义的底部导航
      },
       changeState(e){
        if (!this.data.isDisabled) {   //当disabled=false时
            this.setData({  
              isDisabled: true,  //修改isDisabled的值为true（即启用状态）
              text: "修改信息",    //文字修改为“编辑”
              inputFrame:""
            })
          }
          else {    //当disabled=true时
            this.setData({  
              isDisabled: false,    //修改isDisabled的值为false（即禁用状态）
              text: "保存修改",   //文字修改为“保存”
              inputFrame: "border: 1px solid #ddd"
            })
          }
       },

       image_click: function (e) {
        wx.chooseImage({
          count: 9,
          sizeType: ['original', 'compressed'],
          sourceType: ['album'],
          success: (res) => {
            var list = this.data.lista || []; // 获取已选择的图片列表
            list.push(...res.tempFilePaths); // 将新选择的图片添加到列表中
            this.setData({
              lista: list,
              i: this.data.i + 1 // 将i的值加一
            });
          }
        });
      },
      onChooseAvatar(e) {
        const { avatarUrl } = e.detail
        const { nickName } = this.data.userInfo
        this.setData({
          "userInfo.avatarUrl": avatarUrl,
          hasUserInfo: nickName && avatarUrl && avatarUrl !== defaultAvatarUrl,
        })
      }
})