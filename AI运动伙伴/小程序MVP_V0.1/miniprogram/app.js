const { createInitialState } = require('./data/mock')

App({
  globalData: createInitialState(),

  onLaunch() {
    const cached = wx.getStorageSync('teamo_mvp_state')
    if (cached && cached.profile) {
      const initial = createInitialState()
      const migrated = Object.assign({}, initial, cached)
      migrated.profile = Object.assign({}, initial.profile, cached.profile || {})
      migrated.device = Object.assign({}, initial.device, cached.device || {})
      migrated.tasks = (migrated.tasks || initial.tasks).map(item => Object.assign({}, item, {
        source: item.source === '家庭任务' ? '家长邀请' : item.source,
        receipt: item.receipt || (item.status === '已完成' ? '结果已同步' : '设备已收到')
      }))
      migrated.records = (migrated.records || initial.records).map(item => Object.assign({
        status: '已完成', source: '家长邀请', deviceName: migrated.device.name
      }, item))
      this.globalData = migrated
      wx.setStorageSync('teamo_mvp_state', this.globalData)
    }
  },

  getState() {
    return this.globalData
  },

  updateState(patch) {
    this.globalData = Object.assign({}, this.globalData, patch)
    wx.setStorageSync('teamo_mvp_state', this.globalData)
    return this.globalData
  },

  resetState() {
    this.globalData = createInitialState()
    wx.setStorageSync('teamo_mvp_state', this.globalData)
  }
})
