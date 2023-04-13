import json,random,requests
import time

from common import Common
datas=Common.get_data()
# 所有测试平台接口请求头一致
# 根据手机号查询uid
def getaccountinfo(mode,number):
    global data
    ress = {}
    try:
        number = number.split(',')
        data = []
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://192.168.3.54:8901',
            'Referer': 'http://192.168.3.54:8901/thriftTester/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        # 根据手机号查uid
        if mode=="mobile":
            for mobile in number:
                mobile=str(mobile)
                param={"mobile":str(mobile),"operator": {"opsUid": 0,"ip": "0"}}
                datas = {
                    'params': '{"group":"userservice-facade-ops","scope":"default","url":"","iface":"com.ximalaya.xfm.userservice.facade.ops.thrift.AccountService$Iface","artifactId":"standalone-pom","method":"getUidByMobile","authAapplication":"","isPeakReq":false,"params":%s}'%param,
                }
                # print(datas)
                re =requests.post('http://192.168.3.54:8901/thriftTester/v3/invoke.htm', headers=headers, data=datas,
                                         verify=False)
                content=json.loads(json.loads(re.text)["content"])
                if "value" in content:
                    uid=content["value"]
                    # 再根据uid查询详细信息
                    d=getaccountinfobyuid(uid)
                    data.append(d)
                elif content["present"]==False:
                    d={"mobile":mobile,"msg":"手机号未注册"}
                    data.append(d)
        else:
            for uid in number:
                d=getaccountinfobyuid(uid)
                data.append(d)
        ress["code"]=200
        ress["data"]=data
        ress["message"]="请求成功"
    except Exception as e:
        ress["code"] = 400
        ress["data"] = []
        ress["message"] = "请求失败"
    return ress
def getaccountinfobyuid(uid):
    d = {}
    param = {"uid": int(uid)}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://192.168.3.54:8901',
        'Referer': 'http://192.168.3.54:8901/thriftTester/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    datas = {
        'params': '{"group":"account-combine","scope":"default","url":"","iface":"com.ximalaya.account.combine.thrift.AccountCombineFacade$Iface","artifactId":"standalone-pom","method":"accountIntegrationInfo","authAapplication":"","isPeakReq":false,"params":%s}' % param,
    }
    re = requests.post('http://192.168.3.54:8901/thriftTester/v3/invoke.htm', headers=headers, data=datas,
                       verify=False)
    d["uid"] = int(uid)
    content = json.loads(json.loads(re.text)["content"])
    if "info" in content:
        # 获取其内容转成dict
        info = json.loads((content['info'])[1:-1])
        # print(info,'\n',type(info))
        d["mobile"] = info["mobile"]
        # 是否加V
        d["verify"] = info["verifyInfo"]["verify"]
        # 昵称
        d["nickname"]=info["nickname"]
        # 注册时间
        d["registerTime"]=info["registerTime"]
        d["msg"]="OK"
    elif "errorMsg" in content:
        d["msg"]=content["errorMsg"]
    return d
# 主播实名认证
def certification(uids,isOpenlvb,isOpenGoods):
    uids = uids.split(',')
    ress={}
    data=[]
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://192.168.3.54:8901',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://192.168.3.54:8901/thriftTester/?iface=com.ximalaya.anchor.verify.thrift.AnchorVerifyService$Iface&artifactId=anchor-verify-api&group=anchor-verify&scope=default&method=quickAddAnchorVprofileVerify&reqParam=%7B%0A%20%20%20%20%22vprofileParam%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22uid%22%3A%20123424%2C%0A%20%20%20%20%20%20%20%20%22vstatus%22%3A%20%221%22%2C%0A%20%20%20%20%20%20%20%20%22vtype%22%3A%20%221%22%2C%0A%20%20%20%20%20%20%20%20%22gender%22%3A%201%2C%0A%20%20%20%20%20%20%20%20%22phone%22%3A%20%2213017533238%22%2C%0A%20%20%20%20%20%20%20%20%22email%22%3A%20%221234%40qq.com%22%2C%0A%20%20%20%20%20%20%20%20%22qq%22%3A%20%2213017533238%22%2C%0A%20%20%20%20%20%20%20%20%22address%22%3A%20%22dsafadsf%22%2C%0A%20%20%20%20%20%20%20%20%22ageRange%22%3A%20%22fadsf%22%2C%0A%20%20%20%20%20%20%20%20%22realName%22%3A%20%22yuanzhi%22%2C%0A%20%20%20%20%20%20%20%20%22idCard%22%3A%20%22410726199302144236%22%2C%0A%20%20%20%20%20%20%20%20%22idCardPath%22%3A%20%22234234%22%2C%0A%20%20%20%20%20%20%20%20%22vChannel%22%3A%20%221%22%2C%0A%20%20%20%20%20%20%20%20%22cardType%22%3A%20%22%E4%BA%8C%E4%BB%A3%E8%BA%AB%E4%BB%BD%E8%AF%81%22%2C%0A%20%20%20%20%20%20%20%20%22uname%22%3A%20%22%E9%98%BF%E6%96%AF%E9%A1%BF%E5%8F%91%E9%80%81%E5%88%B0%E5%8F%91%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22opsId%22%3A%203472%0A%7D',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    try:
        for uid in uids:
            uid = int(uid)
            di={}
            di["uid"] = uid
            # 生成随机身份证号
            idCard="511303" + str(random.randint(1970, 2003)) + "0" + str(random.randint(1, 9)) + str(
                random.randint(10, 30)) + "1981"
            params={"vprofileParam": {"uid": uid,
                    "vstatus":"1","vtype":"1","gender": 1,"phone": "16621325482","email":"16621325482@163.com","qq":"13017533238",
                    "address": "dsafadsf","ageRange":"fadsf","realName":"anna","idCard":idCard,"idCardPath":"234234",
                    "vChannel": "1","cardType":"二代身份证","uname":"anna"},"opsId": 22866}
            datas = {
                'params': '{"group":"anchor-verify","scope":"default","url":"","iface":"com.ximalaya.anchor.verify.thrift.AnchorVerifyService$Iface","artifactId":"anchor-verify-api","method":"quickAddAnchorVprofileVerify","authAapplication":"","isPeakReq":false,"params":%s}'%params,
        }
            re = requests.post('http://192.168.3.54:8901/thriftTester/v3/invoke.htm', headers=headers, data=datas, verify=False)
            data.append(di)
            # 构造字典格式的返回响应
            # 实名认证成功
            if json.loads(json.loads(re.text)['content'])['success']:
                di["profileVerify"]='success'
            else:
                di["profileVerify"]=json.loads(json.loads(re.text)['content'])['errorMsg']
            # 返回的响应请求结果生成键值对添加到data中
            if isOpenlvb == True:
                openlvb_status = Openlv(uid)
                di['Openlvb'] = openlvb_status
            else:
                di['Openlvb'] = "false"
            if isOpenGoods == True:
                opengoods_status = open_goods(uid)
                di["OpenGoods"] = opengoods_status
            else:
                di["OpenGoods"] = "false"
            ress["code"] = 200
            ress["data"] = data
            ress["msg"] = "请求成功"
    except Exception as e:
        print(e)
        ress["code"] = 500
        ress["data"] = []
        ress["msg"] = "请求失败，请重试"
    return ress
# 直播实名认证
"""
数据库sql：
INSERT INTO `tb_live_verify_user_info` (`uid`, `real_name`, `id_type`, `id_num`, `country_code`, `hold_id_img_store_id`, `birthdate`, `status`, `refuse_reason`, `verify_time`, `verify_type`, `created_at`, `updated_at`)
VALUES
	(1167510, 'S3oFPbFlPEGmXlPjwbcNfQ==', 1, 'ILFuXZ8epqRiZkr3kFwOsA10LTmEDm10zcwkn09St2Q=', NULL, NULL, '1996-10-05', 1, NULL, 1656841621732, 1, '2022-07-03 17:47:01', '2022-07-03 17:47:01');
redis：
set live_verify_user_cmp_1298182 15  批量set命令：mset key1 value1 key2   value2
"""
# 开通视频直播权限
"""往表tb_live_room_auth里插入数据roomid=id"""
# 开通视直播权限
def Openlv(uid):
#     连接数据库
    database='lamia'
    sql1='select id from tb_live_room where uid=%d'%int(uid)
    # 表tb_live_room根据uid查到对应id
    id=Common.execute_sql(datas['host1'],datas['port1'],'lamia',datas['user'],datas['password'],sql1)
    if id!=None:
        roomid=id[0]
    else:
        return "音频权限fail"
    # print(type(uid),type(roomid))
    sql2='select deleted from tb_live_room_auth where room_id=%d'%int(roomid)
    df=Common.read_sql(datas['host1'],datas['port1'],'lamia',datas['user'],datas['password'],sql2)
    # 判断用户是否已开通视频权限
    if df.empty:
        sql3="INSERT INTO tb_live_room_auth ( `room_id`, `type`, `start_at`, `end_at`, `deleted`, `created_at`, `updated_at`)" \
             "VALUES(%d, 2, now(), now(), 0, now(), now())"%int(roomid)
        res=Common.execute_sql(datas['host1'], datas['port1'], 'lamia', datas['user'], datas['password'], sql3)
        df=Common.read_sql(datas['host1'],datas['port1'],'lamia',datas['user'],datas['password'],sql2)
        if df.empty:
            return "fail"
        else:
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'http://192.168.3.54:8901',
                'Proxy-Connection': 'keep-alive',
                'Referer': 'http://192.168.3.54:8901/thriftTester/index.html',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            }

            data = {
                'params': '{"group":"lamia-base","scope":"default","url":"","iface":"com.ximalaya.lamia.base.business.api.thrift.TLamiaBaseService$Iface","artifactId":"lamia-base-business-api","method":"reloadByUids","authAapplication":"","isPeakReq":false,"params":"{\\n  \\"uids\\": [%d]\\n}"}' % uid,
            }
            response = requests.post('http://192.168.3.54:8901/thriftTester/v3/invoke.htm', headers=headers, data=data,
                                     verify=False)
            print(response.content)
            return "success"
    # 用户已开通视频权限直接返回
    else:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://192.168.3.54:8901',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://192.168.3.54:8901/thriftTester/index.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        data = {
            'params': '{"group":"lamia-base","scope":"default","url":"","iface":"com.ximalaya.lamia.base.business.api.thrift.TLamiaBaseService$Iface","artifactId":"lamia-base-business-api","method":"reloadByUids","authAapplication":"","isPeakReq":false,"params":"{\\n  \\"uids\\": [%d]\\n}"}' % uid,
        }
        response = requests.post('http://192.168.3.54:8901/thriftTester/v3/invoke.htm', headers=headers, data=data,
                                 verify=False)
        print(response.content)
        return "success"
# 用户侧实名
"""sql：
 INSERT INTO `tb_live_verify_user_info` (`uid`, `real_name`, `id_type`, `id_num`, `country_code`, `hold_id_img_store_id`, `birthdate`, `status`, `refuse_reason`, `verify_time`, `verify_type`, `created_at`, `updated_at`)
VALUES (1167510, 'S3oFPbFlPEGmXlPjwbcNfQ==', 1, 'ILFuXZ8epqRiZkr3kFwOsA10LTmEDm10zcwkn09St2Q=', NULL, NULL, '1996-10-05', 1, NULL, 1656841621732, 1, '2022-07-03 17:47:01', '2022-07-03 17:47:01');
#实人认证：1 二要素认证：1  年满18岁：1 用户认证：1
redis：set live_verify_user_cmp_1298182 15 """
# 开通卖货白名单
def open_goods(uid):
    database = 'reserve'
    try:
            da = Common.read_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'],'select * from  tb_white_anchor_new where uid=%d'%(uid))
            # print(da)
            # 判断主播是否已开通权限
            if da.empty:
                sql = "INSERT INTO tb_white_anchor_new (uid) values(%d)"%(uid)
                Common.execute_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'],
                                        sql)
                sql2 = 'SELECT * FROM tb_white_anchor_new where uid=%d' % (uid)
                df = Common.read_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'], sql2)
                # 断言
                if df.empty:
                    return "fail"
                else:
                    return "success"
            else:
                # 判断用户已开通卖货权限直接返回
                return "success"
    except Exception as e:
        return "fail"
if __name__ == '__main__':
    # print(certification('565,322',"false","false"))
    print(getaccountinfo("mobile","1662"))
    # print(getaccountinfobyuid("1294839"))