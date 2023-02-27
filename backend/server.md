# 接口文档
### 实名认证接口
- Path: http://192.168.114.36:8000/AddVprofileVerify
- Method: post
- 接口描述：实名认证

### 请求参数
|    参数名称     | 是否必须 |  参数类型   | 示例      | 备注      |
|:-----------:|:----:|:-------:|:--------|:--------|
|   uid       |  是   | String  | "1213"  | 用户 id   |
|  isOpenlvb  |  否   | Boolean | 默认true  | 是否开通视频直播权限 |
|   cookie    |  否   | String  | "JSESSIONID=6670122F057E726BD6AAEA8895FF58D8" | 是否发送邮件  |
| isOpengoods |  否   | Boolean | 默认true  | 是否开通卖货权限 |
{
"uid":"1213,3435",
"isOpenlvb":true, 
"isOpenGoods":true,
"cookie":"JSESSIONID=BD72577718D20455C1FDABEAF49BBB08; _xmLog=h5&627809bd-3ca9-46da-8136-f49845b87900&process.env.sdkVersion; TB_GTA=%7B%22pf%22%3A%7B%22cd%22%3A%22.ximalaya.com%22%2C%22dr%22%3A0%7D%2C%22uk%22%3A%22639144cfecc04f3691258172%22%7D; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; gfsessionid=ew5dfw0yg6s930cpocalmz26rv110rzc; xm-page-viewid=ops-user-pilot-fe; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221859fede73d133e-0ad48ad2dced7d-17525635-2073600-1859fede73ed69%22%2C%22%24device_id%22%3A%221859fede73d133e-0ad48ad2dced7d-17525635-2073600-1859fede73ed69%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Falidocs.dingtalk.com%2F%22%2C%22%24latest_referrer_host%22%3A%22alidocs.dingtalk.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; sensorsdata2015session=%7B%7D; teambition_private_sid=eyJhdXRoVXBkYXRlZCI6MTY3MDQ2NDcxOTczMiwibG9naW5Gcm9tIjoidGVhbWJpdGlvbiIsInVpZCI6IjYzOTE0NGNmZWNjMDRmMzY5MTI1ODE3MiIsInVzZXIiOnsiX2lkIjoiNjM5MTQ0Y2ZlY2MwNGYzNjkxMjU4MTcyIiwibmFtZSI6IuW8oOaflCIsImVtYWlsIjoicm91LnpoYW5nQHhpbWFsYXlhLmNvbSIsImF2YXRhclVybCI6Imh0dHBzOi8vdGVhbWJpdGlvbmZpbGUueGltYWxheWEuY29tL3RodW1ibmFpbC8wMTJvMzE0YTlhMTE2OWNmNDE2MGZiYTEyOTIwY2NmYjZjODYvdy8yMDAvaC8yMDAiLCJyZWdpb24iOiIiLCJsYW5nIjoiIiwiaXNSb2JvdCI6ZmFsc2UsIm9wZW5JZCI6IiIsInBob25lRm9yTG9naW4iOiIifX0=; teambition_private_sid.sig=Xx2LMmLwnKwWeuRIJEfocRmwkKs; teambition_lang=zh; _const_cas_ticket=cb33a7a661df4ac796fe0dea3d2c1b0b"
}
### 返回数据

```
<!-- cookie已过期 -->
{
    "code":500,
    "data":[

    ],
    "msg":"cookie已过期，请@张柔"
}

<!-- 正常返回 -->
{
    "code":200,
    "data": [
        {
            "uid": "1213",
            "code": 200,
            "profileVerify":"success",
            "OpenGoods": "success",
            "Openlv": "fail",
            
        },
        {
            "uid": "234",
            "profileVerify":"success",
            "code": 203,
            "OpenGoods": "success",
            "Openlv": "fail",
           
        }
        {
            "uid": "345",
            "profileVerify":true,
            "code": 203,
            "OpenGoods": "success",
            "Openlv": "fail",
            
        }
        {
            "uid": "345",
            "profileVerify":true,
            "code": 200,
          
        }
    ]
    "msg":"请求成功"
}
```
### 课程直播接口
- Path: http://192.168.114.36:8000//CreatecourseLive
- Method: post
- 接口描述：创建课程直播

### 请求参数
|    参数名称     | 是否必须 |  参数类型   | 示例      | 备注      |
|:-----------:|:----:|:-------:|:--------|:--------|
|   uid       |  是   | String  | "1213"  | 用户 id   |
|  isOpenlvb  |  否   | Boolean | 默认true  | 是否开通视频直播权限 |
| isOpengoods |  否   | Boolean | 默认true  | 是否开通卖货权限 |
{
"uid":"1213,3435",
"isOpenlvb":true, 
"isOpenGoods":true,
}
### 返回数据

```
<!-- 接口异常返回 -->
{
    "code":500,
    "data":[ ],
    "msg":"请求失败，请重试"
}

<!-- 接口响应正常（包含认证失败的场景） -->
{
    "code":200,
    "data": [
        {
            "uid": "1213",
            "profileVerify":"已认证，请先取消V认证后重新认证",
            "OpenGoods": "success",
            "Openlv": "fail",
            
        },
        {
            "uid": "234",
            "profileVerify":'success'
            "OpenGoods": "success",
            "Openlv": "fail",
           
        }
    ]
    "msg":"请求成功"
}

