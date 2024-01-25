    // 获取数据库信息
    var apiUrl = 'http://43.136.80.11:5000/student_manager/view_signal_student'
    
var app = getApp()
const defaultAvatarUrl = 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0';

Page({
  data: {
    isDisabled:true,  //表示页面加载完成时disabled为启用状态
    text:"修改信息",  //表示按钮初始文字为编辑
    inputFrame: "",
    i: 0,
    stuId:"",
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
        var that = this;
        const head = app.globalData.avatarUrl
        this.setData({
          head: head
        })

       // 获得缓存的用户ID
       wx.getStorage({
             
              key: 'stuId',
              success: function (res) {
                     console.log(res.data);
                     that.setData({
                            stuId: res.data
                          });
                     wx.request({
                            url: apiUrl,
                            method: 'GET',
                            header: {
                              'app': 'wx-app'
                            },
                            data: {
                                'student_id': '2021611001',
                            //    'student_id': that.data.stuId,
                            },
                            success: function (res) {
                                   console.log("xnsacnj",that.data.stuId)
                              if (res.statusCode === 200) {
                                // 接受参数
                                var result = res.data;
                                console.log(result)
                                const stu_name = result.student_information.stu_name
                                const stu_id = result.student_information.stu_id
                                const major = result.student_information.major
                                const email = result.student_information.email
                                const phone = app.globalData.stu_phone_number
                  
                                that.setData({
                                  stu_name: stu_name,
                                  stu_id: stu_id,
                                  major: major,
                                  email: email,
                                  phone: phone
                                })
                  
                                console.log(result)
                                
                                }
                                
                            },
                            fail: function (error) {
                              // 捕捉请求报错
                              console.error('Request failed:', error);
                            }
                          }) 
              }
       });
    


      },
      onInput:function(e){
        //修改电话
        const phone = e.detail.value
        app.globalData.stu_phone_number = phone

        this.setData({
          phone: phone
        })
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

      onChooseAvatar(e) {
        const { avatarUrl } = e.detail;
        const { nickName } = this.data.userInfo;
        app.globalData.avatarUrl = avatarUrl

        this.setData({
          head: app.globalData.avatarUrl,
          hasUserInfo: nickName && avatarUrl && avatarUrl !== defaultAvatarUrl,

        })

      }
})