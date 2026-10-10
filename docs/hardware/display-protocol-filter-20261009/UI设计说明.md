# 显示屏物料库 UI 调整

以企业库存应用的数据操作习惯为参考，保留真实选型数据的状态与来源。

参考来源：

- [SAP Fiori 元素说明](https://www.sap.com/design-system/fiori-design-web/v1-96/discover/get-started/ui-elements-overview)：统一应用框架与控件层级。
- [SAP 库存概览](https://learning.sap.com/courses/inventory-management-in-sap-cloud-erp/using-analytical-apps-for-inventory-management-2)：概览、筛选与明细的组织方式。
- [IBM Carbon 数据表组件](https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/DataTable/DataTable.mdx)：表格工具栏与搜索。

本页采用浅灰底、白色面板、深蓝应用栏与蓝色动作色。默认显示清单，产品图独立切换；行内产品图、采购与验证说明可展开。增加型号/控制器搜索、CSV导出入口与关联硬件方案导航。

候选数与图片数表示研究资料覆盖，不表示库存。未知尺寸、驱动和版本继续明确标注。

检查：脚本执行、默认筛选、触控筛选、搜索、重置、视图切换、无效阈值清空及本地图片存在性通过。浏览器自动化初始化失败，尚未视觉复核布局。
