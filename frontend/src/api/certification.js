import request from '@/utils/request'

// const os = require('os')
// const getIP = () => {
//   const interfaces = os.networkInterfaces()
//   console.log('interfaces:', interfaces)
//   for (const devName in interfaces) {
//     const iface = interfaces[devName]
//     console.log('iface:', iface)
//     for (let i = 0; i < iface.length; i++) {
//       const alias = iface[i]
//       console.log('alias:', alias)
//       if (alias.family === 'IPv4' && alias.address !== '127.0.0.1' && !alias.internal && alias.netmask === '255.255.255.0') {
//         return alias.address
//       }
//     }
//   }
// }
// const domainName = 'http://192.168.114.36:7169/ximalive-qa'

// const domainName = 'http://172.26.53.146:7169/ximalive-qa'
const domainName = 'http://ops.test.ximalaya.com/ximalive-qa'

const api = {
  addVprofileVerify: '/AddVprofileVerify',
  createCourseLive: '/CreatecourseLive'
}
export default api
export function addVprofileVerify (parameter) {
  return request({
    url: domainName + api.addVprofileVerify,
    method: 'POST',
    data: JSON.stringify(parameter),
    headers: {
      'Content-Type': 'application/json;charset=UTF-8',
    }
  })
}

export function createCourseLive (parameter) {
  return request({
    url: domainName + api.createCourseLive,
    method: 'POST',
    data: JSON.stringify(parameter),
    headers: {
      'Content-Type': 'application/json;charset=UTF-8',
    }
  })
}
