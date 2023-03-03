module.exports = {
  // api管理系统，用于获取http应用列表
  opsLogin: "http://ops.ximalaya.com/cas-server/login?locale=zh_CN&service=",
  opsLogout: "http://ops.ximalaya.com/cas-server/logout?locale=zh_CN&service=",
  opsPassport: "http://cms.9nali.com/thriftTester/v3/noauth/invoke.htm",
  thriftTester: "http://192.168.3.54:8901/thriftTester",
  thriftTesterInvoke: "http://192.168.3.54:8901/thriftTester/invoke.htm",
  loginPassport: "https://passport.ximalaya.com/",
  uatPassport: "https://passport.uat.ximalaya.com/",
  testPassport: "https://passport.test.ximalaya.com/",
  workbenchSaveCase:
    "http://yunxiao.xmly.work/workbench/apiresult/saveTestresult",
  localWorkbenchSaveCase:
    "http://127.0.0.1:8000/workbench/apiresult/saveTestresult",
  testWorkbenchSaveCase:
    "http://192.168.60.245:8080/workbench/apiresult/saveTestresult",
  MainstayAdmin: "http://cms.9nali.com/mainstay-admin/", // mainstay后台
};
