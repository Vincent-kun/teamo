const app = getApp()
Page({
  data: { records: [], total: 0, average: 0 },
  onShow() {
    const records = app.getState().records || []
    const average = records.length ? Math.round(records.reduce((sum, item) => sum + item.score, 0) / records.length) : 0
    this.setData({ records, total: records.length, average })
  },
  openRecord(e) { wx.navigateTo({ url: `/pages/analysis/index?id=${e.currentTarget.dataset.id}` }) }
})
