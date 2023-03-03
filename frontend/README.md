文件夹
dist 文件夹：默认 npm run build 命令打包生成的静态资源文件，用于生产部署
node_modules：存放npm命令下载的开发环境和生产环境的依赖包
public：存放项目中需要用到的资源文件，css、js、images以及index
src文件夹：存放项目源码及需要引用的资源文件
src/api文件夹：放ajax相关操作的代码文件:index.js(相关的接口),ajax.js(封装的axios,拦截器)。有的叫service：自己配置的vue请求后台接口方法
src/common文件夹：stylus的混合文件.styl，不要写到public也可以
src/components文件夹：存放vue开发中抽离的一些公共组件
src/mock文件夹：mock数据存放文件及mock模拟接口（没有后台接口或接口不完整情况下可以模拟后台接口）
src/router文件夹:vue-router，路由器及路由的配置
src-store文件夹：存放 vue中的状态数据，用vuex集中管理
App.vue文件：使用标签渲染整个工程的.vue组件
main.js文件：vue-cli工程的入口文件
package.json文件：用于 node_modules资源部 和 启动、打包项目的 npm 命令管理
config 文件夹：主要存放配置文件，用于区分开发环境、线上环境的不同，常用到此文件夹下 config.js 配置开发环境的端口号、是否开启热加载 或者 设置生产环境的静态资源相对路径、是否开启gzip压缩、npm run build 命令打包生成静态资源的名称和路径等
