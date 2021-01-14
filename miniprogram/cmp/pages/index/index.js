//index.js
import naviConfigs from 'navi.js'
//获取应用实例
const app = getApp()

Page({
  data: {
    naviConfigs: naviConfigs,
    motto: '粤客小厨',
    userInfo: {},
    swiper: {
      imgUrls: [{
          id: 1,
          name: '/images/swiper/sl1.jpg'
        },
        {
          id: 1,
          name: '/images/swiper/sl2.jpg'
        },
        {
          id: 1,
          name: '/images/swiper/sl3.jpg'
        }
      ],
      indicatorDots: true, //是否显示面板指示点
      indicatorColor: 'rgba(249,245,236,0.6)',
      indicatorActiveColor: '#FFCC66',
      autoplay: true, //是否自动切换
      interval: 5000, //自动切换时间间隔
      duration: 500, //滑动动画时长
      circular: true //是否自动切换      
    },
    // hasUserInfo: false,
    // canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function() {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },

  onNaviCard(e) {
    let {
      title,
      navigatemark
    } = e.target.dataset
    switch (e.target.dataset.navigatemark) {
      case "book":
        wx.navigateTo({
          url: '/pages/order/order',
        });
        break;
      case "expgoods":
        wx.navigateTo({
          url: '/pages/dishes/dishes',
        });
        break;
      case "discount":
        wx.navigateTo({
          url: '/pages/voucher/voucher',
        });
        break;
      case "new":
        wx.navigateTo({
          url: '/pages/dishes/dishes',
        });
        break;
      case "suggest":
        wx.navigateTo({
          url: '/pages/discuss/discuss',
        });
        break;
      case "map":
        wx.navigateTo({
          url: '/pages/map/map',
        });
        break;
    }

    // wx.navigateTo({
    //   url: '/pages/navigator/content/index?title=' + title + '&navigatemark=' + navigatemark
    // })
  },

  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  }
})