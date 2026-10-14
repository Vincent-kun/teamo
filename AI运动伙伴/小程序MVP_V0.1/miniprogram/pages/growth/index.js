const app = getApp()

Page({
  data: { state: {}, totalValid: 0, completedCount: 0, week: [{label:'一',value:18},{label:'二',value:26},{label:'三',value:0},{label:'四',value:32},{label:'五',value:15},{label:'六',value:22},{label:'日',value:0}] },
  onShow() { const state = app.getState(); const records = state.records || []; this.setData({ state, totalValid: records.reduce((sum, item) => sum + Number(item.valid || 0), 0), completedCount: records.filter(item => item.status === '已完成').length }) },
  openAnalysis() { wx.navigateTo({ url: '/pages/analysis/index' }) },
  openRecords() { wx.navigateTo({ url: '/pages/records/index' }) },
  openPosture() { wx.navigateTo({ url: '/pages/posture/index' }) }
})
