import request from '@/utils/request'
const domainName = 'http://192.168.114.36:80'
const axios = require('axios');
const crypto = require('crypto-browserify'); //引入密码学crypto模块
const thirdUrl = require('../configurl.js');
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
