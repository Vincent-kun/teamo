const app = getApp()
const api = require('../../services/api')
const { actions } = require('../../data/mock')

Page({
  data: { state: {}, latestRecord: null, todayTasks: [], quickActions: actions.filter(item => item.available), progress: 50, statusText: '空闲' },

  onShow() {
    const state = app.getState()
    const done = state.tasks.filter(item => item.status === '已完成').length
    const todayTasks = state.tasks.filter(item => item.status !== '已完成').slice(0, 2)
    const labels = { idle: '空闲可用', ready: '任务已到达', running: '运动进行中', paused: '运动已暂停', completed: '结果待查看', offline: '设备离线', error: '设备异常' }
    this.setData({ state, latestRecord: state.records[0], todayTasks, statusText: labels[state.device.status] || state.device.status, progress: Math.round(done / Math.max(1, state.tasks.length) * 100) })
  },

  openDevice() { wx.navigateTo({ url: '/pages/device/index' }) },
  openAnalysis() { wx.navigateTo({ url: '/pages/analysis/index' }) },
  openAI() { wx.switchTab({ url: '/pages/ai/index' }) },
  openTasks() { wx.switchTab({ url: '/pages/tasks/index' }) },
  openGrowth() { wx.switchTab({ url: '/pages/growth/index' }) },
  openLibrary() { wx.navigateTo({ url: '/pages/library/index' }) },
  openRecords() { wx.navigateTo({ url: '/pages/records/index' }) },
  startAction(e) { wx.navigateTo({ url: `/pages/library/index?id=${e.currentTarget.dataset.id}` }) },

  sendQuickTask() {
    const state = app.getState()
    wx.showLoading({ title: '正在发送' })
    api.sendDeviceCommand(state.device.id, 'START_TASK', { action: 'jumping_jack', targetCount: 20 })
      .then(() => {
        const device = Object.assign({}, state.device, { status: 'ready' })
        app.updateState({ device, latestCommand: { type: 'START_TASK', name: '开合跳', target: 20 } })
        wx.hideLoading()
        wx.showToast({ title: '设备已收到任务' })
        this.onShow()
      })
  }
})
