const app = getApp()
Page({ data: { alerts: 0 }, onShow() { this.setData({ alerts: app.getState().postureAlerts || 0 }) } })
