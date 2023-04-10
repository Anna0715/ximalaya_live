import request from '@/utils/request'

// const domainName = 'http://192.168.114.36:80'
// const domainName = 'http://192.168.114.36:7169/ximalive-qa'
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