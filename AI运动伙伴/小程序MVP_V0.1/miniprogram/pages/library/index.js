const app = getApp()
const api = require('../../services/api')
const { actions } = require('../../data/mock')

Page({
  data: { actions, selected: null, target: 20, sending: false },
  onLoad(options) {
    if (options.id) this.selectById(options.id)
  },
  selectAction(e) { this.selectById(e.currentTarget.dataset.id) },
  selectById(id) {
    const selected = actions.find(item => item.id === id)
    if (selected) this.setData({ selected, target: selected.target })
  },
  closeDetail() { this.setData({ selected: null }) },
  changeTarget(e) { this.setData({ target: Math.max(5, this.data.target + Number(e.currentTarget.dataset.step)) }) },
  startNow() {
    if (this.data.sending || !this.data.selected) return
    if (!this.data.selected.available) return wx.showModal({ title: this.data.selected.stage, content: '该动作已进入产品动作库，但识别规则尚未完成联合验证，当前MVP暂不支持发送到设备。', showCancel: false })
    const state = app.getState()
    if (!state.device.online) return wx.showToast({ title: '设备离线，请先连接', icon: 'none' })
    this.setData({ sending: true })
    api.sendDeviceCommand(state.device.id, 'START_TASK', { action: this.data.selected.id, targetCount: this.data.target }).then(() => {
      app.updateState({ latestCommand: { type: 'START_TASK', name: this.data.selected.name, target: this.data.target }, device: Object.assign({}, state.device, { status: 'ready' }) })
      this.setData({ sending: false })
      wx.showModal({ title: '训练已发送', content: `设备将引导孩子完成 ${this.data.selected.name} ${this.data.target}${this.data.selected.unit}。`, showCancel: false })
    }).catch(() => { this.setData({ sending: false }); wx.showToast({ title: '发送失败，请重试', icon: 'none' }) })
  }
})
