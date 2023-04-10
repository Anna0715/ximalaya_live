// eslint-disable-next-line
import { UserLayout, BasicLayout } from '@/layouts'
import { bxAnaalyse } from '@/core/icons'

const RouteView = {
  name: 'RouteView',
  render: h => h('router-view')
}

export const asyncRouterMap = [
  {
    path: '/',
    name: 'index',
    component: BasicLayout,
    meta: { title: 'menu.home' },
    redirect: '/consumer/certification',
    children: [
      {
        path: '/consumer',
        name: 'consumer',
        redirect: '/consumer/certification',
        component: RouteView,
        meta: { title: 'menu.consumer', keepAlive: false, icon: bxAnaalyse, permission: ['dashboard'] },
        children: [
          {
            path: '/consumer/certification',
            name: 'Certification',
            component: () => import('@/views/consumer/Certification'),
            meta: { title: 'menu.consumer.certification', keepAlive: false, permission: ['dashboard'] }
          },
          {
            path: '/consumer/videoPermissions',
            name: 'VideoPermissions',
            component: () => import('@/views/exception/404'),
            meta: { title: 'menu.consumer.video-permissions', keepAlive: false, permission: ['dashboard'] }
          }
        ]
      },
      {
        path: '/business',
        name: 'business',
        redirect: '/business/createCourseLive',
        component: RouteView,
        meta: { title: 'menu.business', keepAlive: false, icon: bxAnaalyse, permission: ['dashboard'] },
        children: [
          {
            path: '/business/createCourseLive',
            name: 'CreateCourseLive',
            component: () => import('@/views/business/CreateCourseLive.vue'),
            meta: { title: 'menu.business.createCourseLive', keepAlive: false, permission: ['dashboard'] }
          }

        ]
      }
    ]
  },
  {
    path: '*',
    redirect: '/404',
    hidden: true
  }
]

/**
 * 基础路由
 * @type { *[] }
 */
export const constantRouterMap = [
  {
    path: '/user',
    component: UserLayout,
    redirect: '/user/login',
    hidden: true,
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import(/* webpackChunkName: "user" */ '@/views/user/Login')
      }
    ]
  },

  {
    path: '/404',
    component: () => import(/* webpackChunkName: "fail" */ '@/views/exception/404')
  }
]
