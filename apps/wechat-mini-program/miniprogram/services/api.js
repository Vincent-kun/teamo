const USE_MOCK = true
const API_BASE_URL = 'https://api.example.com'

function delay(result, ms = 450) {
  return new Promise(resolve => setTimeout(() => resolve(result), ms))
}

function request(path, options = {}) {
  if (USE_MOCK) return delay({ code: 0, data: options.mockData || {} })
  return new Promise((resolve, reject) => {
    wx.request({
      url: API_BASE_URL + path,
      method: options.method || 'GET',
      data: options.data || {},
      header: { Authorization: `Bearer ${wx.getStorageSync('token') || ''}` },
      success: res => resolve(res.data),
      fail: reject
    })
  })
}

function sendDeviceCommand(deviceId, type, payload) {
  return request(`/devices/${deviceId}/commands`, {
    method: 'POST',
    data: { messageId: `M${Date.now()}`, type, payload, timestamp: Date.now() },
    mockData: { accepted: true, type, payload }
  })
}

function generatePlan(input) {
  const duration = Number(input.duration) || 15
  const plan = {
    id: `P${Date.now()}`,
    name: `${input.goal || '基础体能'} · 7天陪伴计划`,
    summary: `适合${input.age || 8}岁儿童，每次约${duration}分钟`,
    days: [
      { day: 1, items: [{ name: '开合跳', target: 20, unit: '次' }, { name: '深蹲起', target: 12, unit: '次' }] },
      { day: 2, items: [{ name: '高抬腿', target: 30, unit: '次' }, { name: '平板支撑', target: 20, unit: '秒' }] },
      { day: 3, items: [{ name: '轻松活动', target: 10, unit: '分钟' }] },
      { day: 4, items: [{ name: '开合跳', target: 25, unit: '次' }, { name: '深蹲起', target: 15, unit: '次' }] },
      { day: 5, items: [{ name: '高抬腿', target: 40, unit: '次' }] },
      { day: 6, items: [{ name: '亲子挑战', target: 15, unit: '分钟' }] },
      { day: 7, items: [{ name: '拉伸与复盘', target: 10, unit: '分钟' }] }
    ]
  }
  return request('/ai/plans', { method: 'POST', data: input, mockData: plan })
}

module.exports = { USE_MOCK, request, sendDeviceCommand, generatePlan }
