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
| isOpengoods |  否   | Boolean | 默认true  | 是否开通卖货权限 |
{
"uid":"1213,3435",
"isOpenlvb":true, 
"isOpenGoods":true
}
### 返回数据

```
<!-- 接口报错 -->
{
    "code":500,
    "data":[

    ],
    "msg":"请求失败，请重试"
}

<!-- 正常返回 -->
{
    "code":200,
    "data": [
        {
            "uid": "1213",
            "profileVerify":"success",
            "OpenGoods": "success",
            "Openlv": "fail",
            
        },
        {
            "uid": "234",
            "profileVerify":"已认证，请先取消V认证后重新认证",
            "OpenGoods": "success",
            "Openlv": "fail",
           
        }
        {
            "uid": "345",
            "profileVerify":"success",
            "OpenGoods": "success",
            "Openlv": "fail",
            
        }
        {
            "uid": "345",
            "profileVerify":"success",
          
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

