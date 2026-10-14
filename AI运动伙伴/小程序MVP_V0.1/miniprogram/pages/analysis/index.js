const app = getApp()

Page({
  data: { record: {}, completion: 0, validRate: 0, recordId: '' },
  onLoad(options) { this.setData({ recordId: options.id || '' }) },
  onShow() {
    const records = app.getState().records || []
    const record = records.find(item => item.id === this.data.recordId) || records[0]
    if (!record) return
    this.setData({ record, completion: Math.round(record.actual / record.target * 100), validRate: Math.round(record.valid / Math.max(1, record.actual) * 100) })
  }
})
