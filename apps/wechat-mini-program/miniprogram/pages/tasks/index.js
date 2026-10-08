const app = getApp()
const api = require('../../services/api')
const { actions } = require('../../data/mock')

Page({
  data: {
    state: {}, visibleTasks: [], filter: 'today', actions: actions.filter(item => item.available), showCreate: false, lastReceipt: '',
    taskType: 'action', selected: 'jumping_jack', target: 20, schedule: 'once', scheduledTime: '19:00',
    submitting: false,
    schedules: [
      { id: 'once', name: '仅今天' },
      { id: 'daily', name: '每天打卡' },
      { id: 'alternate', name: '隔天一次' }
    ]
  },

  onShow() { this.refreshTasks(this.data.filter) },
  refreshTasks(filter) {
    const state = app.getState()
    const visibleTasks = (state.tasks || []).filter(item => {
      if (filter === 'done') return item.status === '已完成' || item.status === '已取消' || item.status === '异常结束'
      if (filter === 'future') return item.status === '已计划' || (item.time || '').indexOf('明天') >= 0
      return item.status !== '已完成' && item.status !== '已计划'
    })
    this.setData({ state, visibleTasks, filter })
  },
  setFilter(e) { this.refreshTasks(e.currentTarget.dataset.value) },
  openCreate() {
    this.setData({ showCreate: true, taskType: 'action', selected: 'jumping_jack', target: 20, schedule: 'once', scheduledTime: '19:00', submitting: false })
  },
  closeCreate() { this.setData({ showCreate: false }) },
  chooseAction(e) {
    const selected = e.currentTarget.dataset.id
    const action = actions.find(item => item.id === selected)
    this.setData({ selected, target: action.target })
  },
  chooseSchedule(e) { this.setData({ schedule: e.currentTarget.dataset.id }) },
  chooseType(e) {
    const taskType = e.currentTarget.dataset.value
    if (taskType === 'plan' && !(app.getState().plans || []).length) {
      wx.showToast({ title: '请先到AI页生成计划', icon: 'none' })
      return
    }
    this.setData({ taskType })
  },
  chooseTime(e) { this.setData({ scheduledTime: e.detail.value }) },
  changeTarget(e) { this.setData({ target: Math.max(5, this.data.target + Number(e.currentTarget.dataset.step)) }) },
  cancelTask(e) {
    const id = e.currentTarget.dataset.id
    const state = app.getState()
    const task = (state.tasks || []).find(item => item.id === id)
    if (!task) return
    wx.showModal({ title: '取消这项运动？', content: '取消后设备将停止提醒，已产生的运动记录不会删除。', success: res => {
      if (!res.confirm) return
      api.sendDeviceCommand(state.device.id, 'CANCEL_TASK', { taskId: id }).then(() => {
        const tasks = state.tasks.map(item => item.id === id ? Object.assign({}, item, { status: '已取消', receipt: '设备已确认取消' }) : item)
        app.updateState({ tasks })
        this.refreshTasks('today')
        wx.showToast({ title: '任务已取消' })
      })
    } })
  },

  sendTask() {
    if (this.data.submitting) return
    const state = app.getState()
    const plan = (state.plans || [])[0]
    const action = this.data.taskType === 'plan' && plan ? { id: plan.id, name: plan.name, target: plan.days[0].items.length, unit: '组' } : actions.find(item => item.id === this.data.selected)
    if (!action) {
      wx.showToast({ title: '请先选择运动', icon: 'none' })
      return
    }
    if (!state.device || !state.device.id) {
      wx.showToast({ title: '请先绑定设备', icon: 'none' })
      return
    }
    if (!state.device.online) {
      wx.showToast({ title: '设备离线，暂时无法发送', icon: 'none' })
      return
    }
    this.setData({ submitting: true })
    wx.showLoading({ title: '发送中' })
    const scheduleItem = this.data.schedules.find(item => item.id === this.data.schedule)
    const scheduleName = scheduleItem ? scheduleItem.name : '仅今天'
    const time = this.data.schedule === 'once' ? `今天 ${this.data.scheduledTime}` : `${scheduleName} ${this.data.scheduledTime}`
    const finalTarget = this.data.taskType === 'plan' ? action.target : this.data.target
    api.sendDeviceCommand(state.device.id, 'CREATE_TASK', { taskType: this.data.taskType, actionId: action.id, name: action.name, targetCount: finalTarget, schedule: this.data.schedule, time: this.data.scheduledTime })
      .then(() => {
        const nextFilter = this.data.schedule === 'once' ? 'today' : 'future'
        const task = { id: `T${Date.now()}`, actionId: action.id, name: action.name, target: finalTarget, unit: action.unit, source: this.data.taskType === 'plan' ? 'AI计划' : '家长邀请', time, status: this.data.schedule === 'once' ? '待执行' : '已计划', receipt: '设备已收到' }
        app.updateState({ tasks: [task].concat(state.tasks || []), latestCommand: task })
        wx.hideLoading()
        this.setData({ showCreate: false, submitting: false, lastReceipt: `${action.name}已送达 ${state.device.name}` })
        this.refreshTasks(nextFilter)
        wx.showToast({ title: this.data.schedule === 'once' ? '邀请已发送' : '计划已创建' })
      })
      .catch(() => {
        wx.hideLoading()
        this.setData({ submitting: false })
        wx.showToast({ title: '布置失败，请重试', icon: 'none' })
      })
  },
  noop() {}
})
