const app = getApp()
const api = require('../../services/api')
const { actions } = require('../../data/mock')

Page({
  data: { state: {}, count: 0, target: 20, running: false, timer: null, currentAction: { id: 'jumping_jack', name: '开合跳' }, statusText: '空闲可用' },

  onShow() {
    const state = app.getState()
    const command = state.latestCommand || {}
    const action = actions.find(item => item.id === command.action || item.name === command.name) || { id: 'jumping_jack', name: command.name || '开合跳', unit: '次' }
    const labels = { idle: '空闲可用', ready: '任务已到达', running: '运动进行中', paused: '运动已暂停', completed: '运动已完成', offline: '设备离线', error: '设备异常' }
    this.setData({ state, currentAction: action, target: Number(command.target) || this.data.target, statusText: labels[state.device.status] || state.device.status })
  },
  onUnload() { if (this.data.timer) clearInterval(this.data.timer) },

  toggleOnline() {
    const state = app.getState()
    const device = Object.assign({}, state.device, { online: !state.device.online, status: state.device.online ? 'offline' : 'idle' })
    app.updateState({ device })
    this.onShow()
    wx.showToast({ title: device.online ? '设备已上线' : '设备已离线', icon: 'none' })
  },

  start() {
    const state = app.getState()
    if (!state.device.online) return wx.showToast({ title: '请先连接设备', icon: 'none' })
    if (!state.device.camera) return wx.showModal({ title: '摄像头已关闭', content: '动作识别需要摄像头。请先打开摄像头能力并确认物理遮挡已移开。', showCancel: false })
    api.sendDeviceCommand(state.device.id, 'START_TASK', { action: this.data.currentAction.id, targetCount: this.data.target }).then(() => {
      const device = Object.assign({}, state.device, { status: 'running' })
      app.updateState({ device })
      const timer = setInterval(() => {
        if (!this.data.running) return
        const next = Math.min(this.data.target, this.data.count + 1)
        this.setData({ count: next })
        if (next >= this.data.target) this.finish()
      }, 900)
      this.setData({ state: app.getState(), running: true, timer })
    })
  },

  pause() {
    const state = app.getState()
    const running = !this.data.running
    api.sendDeviceCommand(state.device.id, running ? 'RESUME_WORKOUT' : 'PAUSE_WORKOUT', {}).then(() => {
      const device = Object.assign({}, state.device, { status: running ? 'running' : 'paused' })
      app.updateState({ device })
      this.setData({ running })
      this.onShow()
    })
  },

  finish() {
    if (this.data.timer) clearInterval(this.data.timer)
    const state = app.getState()
    const actual = Math.max(1, this.data.count)
    const finished = actual >= this.data.target
    const record = { id: `R${Date.now()}`, name: this.data.currentAction.name, date: '刚刚', actual, target: this.data.target, valid: Math.max(1, actual - 2), duration: actual * 2, score: Math.min(96, 70 + actual), status: finished ? '已完成' : '未完成', source: '家长邀请', deviceName: state.device.name, issues: finished ? ['2次动作幅度不足'] : ['任务提前结束'] }
    const device = Object.assign({}, state.device, { status: 'completed' })
    const tasks = (state.tasks || []).map((item, index) => index === 0 && (item.status === '待执行' || item.status === '已计划') ? Object.assign({}, item, { status: finished ? '已完成' : '异常结束', receipt: '结果已同步' }) : item)
    app.updateState({ device, tasks, records: [record].concat(state.records), todayMinutes: state.todayMinutes + Math.max(1, Math.ceil(record.duration / 60)) })
    this.setData({ running: false, timer: null })
    this.onShow()
    wx.showToast({ title: '运动结果已保存' })
  },
  openAnalysis() { wx.navigateTo({ url: '/pages/analysis/index' }) },
  toggleFeature(e) {
    const state = app.getState()
    const key = e.currentTarget.dataset.key
    const device = Object.assign({}, state.device, { [key]: e.detail.value })
    app.updateState({ device })
    this.setData({ state: app.getState() })
    if (key === 'camera' && !e.detail.value) wx.showToast({ title: '摄像头已关闭，动作识别不可用', icon: 'none' })
  }
})
