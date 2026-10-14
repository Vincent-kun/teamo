const app = getApp()

Page({
  data: { state: {} },
  onShow() { this.setData({ state: app.getState() }) },
  openDevice() { wx.navigateTo({ url: '/pages/device/index' }) },
  openProfile() { wx.navigateTo({ url: '/pages/profile/index' }) },
  toggleSetting(e) {
    const key = e.currentTarget.dataset.key
    const value = e.detail.value
    app.updateState({ [key]: value })
    this.onShow()
  },
  showPrivacy() { wx.showModal({ title: '隐私与儿童数据', content: 'MVP仅保存任务、动作结果和必要的姿态事件；默认不长期保存原始视频。摄像头状态应在设备与小程序中清晰可见。', showCancel: false }) },
  showHelp() { wx.showModal({ title: '使用帮助', content: '先连接设备，再到“任务”或“动作库”发送运动。设备完成识别后，结果会同步到“成长”和“运动记录”。', showCancel: false }) },
  resetDemo() {
    wx.showModal({ title: '重置演示数据', content: '任务、计划和运动记录将恢复到初始状态。', success: res => { if (res.confirm) { app.resetState(); this.onShow(); wx.showToast({ title: '已重置' }) } } })
  }
})
