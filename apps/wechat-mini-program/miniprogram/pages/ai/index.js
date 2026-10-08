const app = getApp()
const api = require('../../services/api')

Page({
  data: {
    form: { age: 8, goal: '增强体能', duration: 15, level: '基础' },
    goals: ['增强体能', '提高协调性', '改善运动习惯'],
    durations: [10, 15, 20],
    levels: ['入门', '基础', '进阶'],
    plan: null,
    loading: false,
    quickQuestions: ['今天适合练什么？', '动作太快怎么办？', '每次练多久合适？'],
    aiAnswer: '', customQuestion: ''
  },

  onShow() {
    const state = app.getState()
    this.setData({ plan: state.plans[0] || null, 'form.age': state.profile.age })
  },
  openLatestAnalysis() { wx.navigateTo({ url: '/pages/analysis/index' }) },
  chooseGoal(e) { this.setData({ 'form.goal': e.currentTarget.dataset.value }) },
  chooseDuration(e) { this.setData({ 'form.duration': Number(e.currentTarget.dataset.value) }) },
  chooseLevel(e) { this.setData({ 'form.level': e.currentTarget.dataset.value }) },
  changeAge(e) { this.setData({ 'form.age': Math.max(4, Math.min(15, this.data.form.age + Number(e.currentTarget.dataset.step))) }) },
  askQuick(e) {
    const question = e.currentTarget.dataset.question
    const answers = {
      '今天适合练什么？': '结合最近记录，今天可以先做 10 分钟协调训练：开合跳 20 次、深蹲起 15 次，中间休息 1 分钟。',
      '动作太快怎么办？': '先把动作做完整再提速。设备会重点提醒节奏和幅度，不需要为了次数牺牲动作质量。',
      '每次练多久合适？': '当前建议每次 10–15 分钟，完成后根据孩子的疲劳感和动作质量再决定是否增加。'
    }
    this.setData({ aiAnswer: answers[question] })
  },
  inputQuestion(e) { this.setData({ customQuestion: e.detail.value }) },
  askCustom() {
    const question = this.data.customQuestion.trim()
    if (!question) return wx.showToast({ title: '先写下你的问题', icon: 'none' })
    this.setData({ aiAnswer: `根据${app.getState().profile.childName}最近的运动记录，建议先保持每次10–15分钟、动作完整优先。关于“${question}”，当前演示版会在接入AI服务后给出更个性化的回答。`, customQuestion: '' })
  },
  newPlan() { this.setData({ plan: null }) },

  generate() {
    this.setData({ loading: true })
    api.generatePlan(this.data.form).then(res => {
      const state = app.getState()
      const plan = res.data
      app.updateState({ plans: [plan].concat(state.plans.filter(item => item.id !== plan.id)) })
      this.setData({ plan, loading: false })
      wx.showToast({ title: '计划已生成' })
    }).catch(() => {
      this.setData({ loading: false })
      wx.showToast({ title: '生成失败', icon: 'error' })
    })
  },

  sendPlan() {
    const state = app.getState()
    const today = this.data.plan.days[0]
    wx.showLoading({ title: '发送中' })
    api.sendDeviceCommand(state.device.id, 'START_PLAN', { planId: this.data.plan.id, items: today.items })
      .then(() => {
        app.updateState({ latestCommand: { type: 'START_PLAN', name: this.data.plan.name, items: today.items }, device: Object.assign({}, state.device, { status: 'ready' }) })
        wx.hideLoading()
        wx.showToast({ title: '已发送今天计划' })
      })
  }
})
