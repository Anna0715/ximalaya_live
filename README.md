# ximalaya_live
实名认证
post /AddVprofileVerify
接口入参：（json）
{"uid":1213, //string
"isOpenlvb":true, //是否开通视频直播权限，false开通，true不开通
"cookie":"JSESSIONID=6670122F057E726BD6AAEA8895FF58D8",
"isOpengoods":true,是否开通卖货权限//"}
接口出参:
{
    "1213": {
        "code": 200,
        "msg": "用户认证成功+视频直播权限开通成功"
    },
    "234": {
        "code": 203,
        "msg": "用户已认证，视频直播权限开通失败"
    }
}