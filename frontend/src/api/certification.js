import request from '@/utils/request'

const domainName = 'http://192.168.114.36:80'

const api = {
  addVprofileVerify: '/AddVprofileVerify'
}


export default api

export function addVprofileVerify (parameter) {
  return request({
    url: domainName + api.addVprofileVerify,
    method: 'POST',
    data: JSON.stringify(parameter),
    headers: {
      'Content-Type': 'application/json;charset=UTF-8'
    }
  })
}
