const actions = [
  { id: 'jumping_jack', name: '开合跳', short: '开', target: 20, unit: '次', type: '协调与心肺', color: 'purple', stage: 'MVP已支持', available: true, hint: '手脚同步，动作打开到位', guide: '双脚打开时双手举过头顶，合拢时回到身体两侧。' },
  { id: 'squat', name: '深蹲起', short: '蹲', target: 15, unit: '次', type: '下肢力量', color: 'peach', stage: 'MVP已支持', available: true, hint: '膝盖朝脚尖方向，起身站稳', guide: '双脚与肩同宽，臀部向后下沉，再平稳站起。' },
  { id: 'high_knee', name: '高抬腿', short: '抬', target: 30, unit: '次', type: '心肺与节奏', color: 'blue', stage: '算法评审中', available: false, hint: '抬腿到合适高度，身体保持直立', guide: '左右交替抬膝，目视前方，不要过度后仰。' },
  { id: 'jump_rope', name: '双脚跳绳', short: '跳', target: 30, unit: '次', type: '协调与心肺', color: 'pink', stage: '后续适配', available: false, hint: '双脚轻落地，保持均匀节奏', guide: '站在镜头前保持全身可见，双脚同时起跳，手臂自然摆动。' },
  { id: 'push_up', name: '俯卧撑', short: '撑', target: 8, unit: '次', type: '上肢力量', color: 'mint', stage: '后续适配', available: false, hint: '身体保持直线，按能力完成', guide: '双手略宽于肩，身体保持稳定；可选择跪姿降低难度。' },
  { id: 'sit_up', name: '仰卧起坐', short: '起', target: 12, unit: '次', type: '核心力量', color: 'pink', stage: '后续适配', available: false, hint: '动作平稳，不用猛拉颈部', guide: '屈膝平躺，腹部发力坐起，再缓慢回落。' },
  { id: 'plank', name: '平板支撑', short: '稳', target: 30, unit: '秒', type: '核心稳定', color: 'blue', stage: '后续适配', available: false, hint: '头、背、腿保持一条直线', guide: '手肘位于肩部下方，收紧腹部，避免塌腰或抬臀。' }
]

function createInitialState() {
  return {
    profile: { parentName: '夏先生', childName: '小夏', age: 8, grade: '小学二年级', goal: '增强体能' },
    device: { id: 'TEAMO-DEMO-001', name: '客厅运动伙伴', online: true, status: 'idle', battery: 82, wifi: '家庭 Wi-Fi', camera: true, voice: true, posture: true, proactive: true, quiet: false },
    todayMinutes: 22,
    streak: 5,
    stars: 46,
    postureAlerts: 2,
    tasks: [
      { id: 'T001', actionId: 'jumping_jack', name: '开合跳', target: 20, unit: '次', source: '家长邀请', time: '今天 19:00', status: '待执行', receipt: '设备已收到' },
      { id: 'T002', actionId: 'squat', name: '深蹲起', target: 15, unit: '次', source: '家长邀请', time: '今天 18:20', status: '已完成', receipt: '结果已同步' }
    ],
    plans: [],
    records: [
      { id: 'R001', name: '深蹲起', date: '今天 18:20', actual: 15, target: 15, valid: 13, duration: 65, score: 86, status: '已完成', source: '家长邀请', deviceName: '客厅运动伙伴', issues: ['2次动作幅度不足'] },
      { id: 'R002', name: '开合跳', date: '昨天 19:10', actual: 20, target: 20, valid: 18, duration: 42, score: 91, status: '已完成', source: '家长邀请', deviceName: '客厅运动伙伴', issues: ['节奏稳定'] }
    ],
    latestCommand: null,
    deviceTimeline: [
      { time: '18:20', text: '完成深蹲起，结果已同步' },
      { time: '17:58', text: '设备上线，网络状态良好' },
      { time: '昨天', text: '完成开合跳 20 次' }
    ],
    notifications: true,
    privacyNotice: true
  }
}

module.exports = { actions, createInitialState }
