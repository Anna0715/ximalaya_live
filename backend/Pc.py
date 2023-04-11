import datetime
import random,requests,json,time
from client import open_goods
from common import Common
datas=Common.get_data()
# 添加课程直播白名单
def addCourselivewhitelist(uids):
    uids=uids.split(',')
    database='diablo'
    try:
        for uid in uids:
            uid = int(uid)
            da = Common.execute_sql(datas['host1'], datas['port1'],database , datas['user'], datas['password'], 'select is_deleted from tb_white_anchor where uid=%d' % (uid))
            # pd.set_option('display.max_columns', None)
            sub_categoryId=random.randint(100001,100009)
            # 判断主播是否已开通权限
            if da==None:
                sql1="INSERT INTO tb_white_anchor (uid,apply_name,dept_name,reason,ops_id,created_at,updated_at,sub_categoryId,is_deleted,audit_director) " \
                     "VALUES(%d, 'autotest', '互娱', '加入白名单', 1,now(), now(), %d, 0, '张柔' )"%(uid,sub_categoryId)
                da = Common.execute_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'],sql1)
                sql2='SELECT * FROM tb_white_anchor where uid=%d' % (uid)
                df = Common.read_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'],sql2)
                # 断言
                if df.empty:
                    return "fail"
                else:
                    return "success"
            else:
                if da[0]==0:
                    return "success"
    except Exception as e:
        return e
# 开通卖货白名单
# 创建课程直播
"""{
  "name":"直播标题",
  "coverPath":"http://group1/M00/77/49/wKgDpl114EyAbLQ1AAAfjf4B9FY39.jpeg", // 直播封面
  "description":"直播简介",
  "uid":57022, // 指定主播
  "booking":true, // 是否预告，true：有预告
  "startAt":2737487484, // 预告开始时间(毫秒)
  "endAt":26737378, // 预告结束时间(毫秒)
  "adminUids":[123, 456, 789], // 管理员uid列表(全量更新，如果为空则删除全部管理员)
  "categoryId":257, // 直播目录(第三级目录id)
  "showPlayBack":true // 是否显示回放, true:显示回放
  "isAutoPull":"true", // 是否自动开启拉流直播
  "pullPath":"xxxxxx", // 拉流直播地址
  "notifyFans":true // 是否通知粉丝，true:通知粉丝
  "pushStreamType":1 // 推流方式 1：电脑直播 2：拉流直播 3：第三方推流直播
  "screenSize":true // 屏幕尺寸
  "openGoods":true // 本场直播是否卖货
  "openGift":true // 是否开启送礼
  "forbidSpeak":true // 直播间禁用评论功
  "detailDescription":"xxxxxxxxxx"; // 详细介绍
  "price":"10.5"; // 价格
  "quantity":100; // 库存
}
"""
def create_course_live(uids,coursetype,openGoods,openGift,showPlayback,startAt,endAt,price,quantity,clearRate):
    # 开通课程直播白名单
    addCourselivewhitelist(uids)
    # 开通主播卖货白名单
    open_goods(uids)
    uids=uids.split(',')
    isTest="false"
    isPaid="false"
    detailDescription=" "
    method="createLive"
    # 正式测试直播默认值
    Referer='http://192.168.3.54:8901/thriftTester/?iface=com.ximalaya.live.fans.club.api.thrift.TFansClubService$Iface&artifactId=live-fans-club-api&group=live-fans-club&scope=default&ip=172.26.6.141&port=2108&method=setRelationNoActive&reqParam=%7B%0A%20%20%22fansUid%22%3A%201244267%2C%0A%20%20%22anchorUid%22%3A%201155190%0A%7D'
    if coursetype == "付费":
        # Referer='http://192.168.3.54:8901/thriftTester/'
        isPaid = "true"
        detailDescription = "http://audi otest.cos.tx.xmcdn.com/storages/79c4-audiotest/E1/C1/GKwaCHkHgdshAACHywAAmyiF.jpg"
        method="createLiveWithPaid"
    # 如果没有传参就给个默认值
    if coursetype == "测试":
        isTest ="true"
    if showPlayback=="":
        showPlayback="false"
    if openGoods=="":
        openGoods="true"
    if openGift=="":
        openGift="true"
    if price=="":
        price="10"
    if quantity=="":
        quantity=1000
    if clearRate=="":
        clearRate=50
    # 默认开始时间：当前时间+20Min,持续30Min
    if startAt=="" or endAt=="":
        startAt=(datetime.datetime.now()+datetime.timedelta(minutes=20)).strftime("%Y-%m-%d %H:%M:%S")
        endAt=(datetime.datetime.now()+datetime.timedelta(minutes=50)).strftime("%Y-%m-%d %H:%M:%S")
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://192.168.3.54:8901',
        'Referer':Referer,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    global content,re,ress
    # 转时间戳(毫秒)
    startime = int(round(time.mktime(time.strptime(startAt, '%Y-%m-%d %H:%M:%S')) * 1000))
    endtime = int(round(time.mktime(time.strptime(endAt, '%Y-%m-%d %H:%M:%S')) * 1000))
    print(startime)
    name = str(startime) + '造数' + coursetype + '直播'
    ress={}
    data=[]
    try:
        for uid in uids:
            d={}
            d["uid"]=uid
            param={
            "input": {
                "roomId": 100001, #房间id
                "name": name,
                "coverPath": "http://audiotest.cos.tx.xmcdn.com/storages/6729-audiotest/1F/95/GKwaCHkHfw1CAAhAOwAAmwrL.jpeg",
                "uid": int(uid),
                "openGift":openGift,
                "description": "课程直播测造数",
                "canbooking":"true",
                "categoryId": 100101,
                "showPlayback":showPlayback,
                "screenSize": "true",
                "notifyFans":"true",
                "isAutoPull": "false",
                "non_recommended": "true",
                "isTest": isTest,
                "pushStreamType": 1,
                "openGoods": openGoods,
                "detailDescription": detailDescription,
                "isPaid": isPaid,
                "forbidSpeak": "false",
                "clearRate":clearRate,
                "price": str(price),
                "quantity":quantity,
                "startAt":startime,
                "endAt":endtime
            }
        }
            params = {
                'params': '{"group":"diablo-live","scope":"default","url":"","iface":"com.ximalaya.diablo.live.business.api.thrift.TDiabloLiveService$Iface","artifactId":"diablo-live-business-api","method":"%s","authAapplication":"","isPeakReq":false,"params":%s}'%(method,param),
            }
            print(params)
            re = requests.post('http://192.168.3.54:8901/thriftTester/v3/invoke.htm', headers=headers, data=params,verify=False)
            #     获取code的内容
            print("响应"+re.text)
            content=json.loads(re.text)["content"]
            print("内容",content)
            content=json.loads(content)
            # 响应code含义：0:成功// 10：该时间段已有直播 9:开始时间需大于当前时间
            if "liveRecord" in content:
                content=content["liveRecord"]
            print("实际",content)
            if content["code"]==0:
                d["CeatecourseLive"]="success"
                d["msg"]="创建"+coursetype+"课程直播场次成功"
            elif content["code"]==10:
                d["CeatecourseLive"]="fail"
                d["msg"]="创建失败，预告时间冲突"
            elif content["code"]==9:
                d["CeatecourseLive"]="fail"
                d["msg"]="预告开始时间需大于当前时间"
            elif content["code"]==-1:
                d["CeatecourseLive"] = "fail"
                d["msg"] = "创建失败，请检查请求参数"
            d["code"]=content["code"]
            data.append(d)
        ress["code"]=200
        ress["data"] = data
        ress["msg"]="请求成功"
    except Exception as e:
        print(e,re.text)
        ress["code"]=500
        ress["data"] = data
        ress["msg"] = "请求失败，请@张柔"
    return ress
# 公会
"""创建公会账号:成立条件：laima.tb_family表里有数据且有蓝v认证
相关库表记录：https://alidocs.dingtalk.com/i/nodes/mdvQnONayjBJKgrD0KpLJPY2MeXzp5o0
数据库:192.168.60.11/lamia
公会入驻申请：tb_family_enter_apply_info
申请视频业务：tb_family
主播入会时间表:tb_family_member_contract
主播开播时间:live_record_all
退转会记录表:tb_family_member_contract
新主播表:tb_anchor_clearing_type
有效新增主播&有效主播表:tb_anchor_clearing_effective_type
新主播结算类型表:tb_anchor_clearing_type
"""
#创建公会账号

def create_family_account():
    # 提交入驻资料申请
    sql1="INSERT INTO `tb_family_enter_apply_info` (`uid`, `warrent_person_info_id`, `company_id`, `family_info_id`, `contract_id`, `anchor_verify_center_status`, `verify_center_status`, `status`, `warrent_person_info_status`, `company_info_status`, `family_info_status`, `ops_id`, `operator`, `verify_refuse_reason`, `filed_time`, `created_at`, `updated_at`, `operator_ops_id`, `request_enterprise_reg_fail_msg`, `anchor_verify_center_update_time`) " \
        "VALUES (1304049, 252, 237, 185, NULL, 0, 0, 205, 1, 1, 1, NULL, NULL, NULL, NULL, now(), now(), NULL, NULL, NULL)"
    da = Common.execute_sql(datas['host1'], datas['port1'], 'lamia', datas['user'], datas['password'], sql1)
if __name__ == '__main__':
    # addCourselivewhitelist("1304329")
    print(create_course_live("1306260","付费","true","true","true","2023-04-18 10:58:49","2023-04-18 11:58:49",5,100,50))