const app = getApp()
Page({
  data: { form: {}, initial: '童', goals: ['增强体能', '提高协调性', '养成运动习惯'] },
  onLoad() { const form = Object.assign({}, app.getState().profile); this.setData({ form, initial: (form.childName || '童').charAt(0) }) },
  inputName(e) { const childName = e.detail.value; this.setData({ 'form.childName': childName, initial: (childName || '童').charAt(0) }) },
  inputGrade(e) { this.setData({ 'form.grade': e.detail.value }) },
  changeAge(e) { this.setData({ 'form.age': Math.max(4, Math.min(15, this.data.form.age + Number(e.currentTarget.dataset.step))) }) },
  chooseGoal(e) { this.setData({ 'form.goal': e.currentTarget.dataset.value }) },
  save() {
    if (!this.data.form.childName.trim()) return wx.showToast({ title: '请填写孩子称呼', icon: 'none' })
    app.updateState({ profile: this.data.form })
    wx.showToast({ title: '已保存' })
    setTimeout(() => wx.navigateBack(), 500)
  }
})
