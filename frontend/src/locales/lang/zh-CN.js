import antd from 'ant-design-vue/es/locale-provider/zh_CN'
import momentCN from 'moment/locale/zh-cn'

import menu from './zh-CN/menu'
import user from './zh-CN/user'
import certification from './zh-CN/certification'

const components = {
  antLocale: antd,
  momentName: 'zh-cn',
  momentLocale: momentCN
}

export default {
  message: '-',

  'layouts.usermenu.dialog.title': '信息',
  'layouts.usermenu.dialog.content': '您确定要注销吗？',
  'layouts.userLayout.title': 'Ant Design 是西湖区最具影响力的 Web 设计规范',
  ...components,
  ...global,
  ...menu,
  ...user,
  ...certification
}
