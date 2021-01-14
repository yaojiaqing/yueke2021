// pages/map/map.js
//获取应用实例
const app = getApp()

let plugin = requirePlugin("myPlugin")
let routeInfo = {
  // startLat: 39.90469,    //起点纬度 选填
  // startLng: 116.40717,    //起点经度 选填
  // startName: "我的位置",   // 起点名称 选填
  endLat: 38.9256500000,    // 终点纬度必传
  endLng: 121.6424600000,  //终点经度 必传
  endName: "大连市同顺街4号 粤客美食",  //终点名称 必传
  mode: "car"  //算路方式 选填
}

Page({
  data: {
    routeInfo: routeInfo
  }
})


// Page({
//   data: {
//     longitude: 121.6424600000,
//     latitude: 38.9256500000,
//     speed: 0,
//     accuracy: 0
//   },
//   //事件处理函数
//   bindViewTap: function () {

//   },
//   onLoad: function () {
//     var that = this
//     wx.showLoading({
//       title: "定位中",
//       mask: true
//     })
//     wx.getLocation({
//       type: 'gcj02',
//       altitude: true,//高精度定位
//       //定位成功，更新定位结果
//       success: function (res) {
//         var latitude = res.latitude
//         var longitude = res.longitude
//         var speed = res.speed
//         var accuracy = res.accuracy

//         that.setData({
//           longitude: longitude,
//           latitude: latitude,
//           speed: speed,
//           accuracy: accuracy
//         })
//       },
//       //定位失败回调
//       fail: function () {
//         wx.showToast({
//           title: "定位失败",
//           icon: "none"
//         })
//       },

//       complete: function () {
//         //隐藏定位中信息进度
//         wx.hideLoading()
//       }

//     })
//   },
// })