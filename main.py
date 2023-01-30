import  requests,random,json,time
from flask import Flask,jsonify,request,Blueprint
from common import Common
from manage import app
Client=Blueprint('Client',__name__)
# app = Flask(__name__)#创建一个服务，赋值给APP
datas=Common.get_data()
# 主播实名认证+开通视频权限
@app.route('/AddVprofileVerify',methods=['post'])
def Certification():
    global res
    try:
        # uid字段：多个uid以英文,分隔
        uids=request.json.get('uid').split(',')
        cookie=request.json.get('cookie')
        # cookie='JSESSIONID=6670122F057E726BD6AAEA8895FF58D8; _xmLog=h5&627809bd-3ca9-46da-8136-f49845b87900&process.env.sdkVersion; teambition_lang=zh; TB_GTA=%7B%22pf%22%3A%7B%22cd%22%3A%22.ximalaya.com%22%2C%22dr%22%3A0%7D%2C%22uk%22%3A%22639144cfecc04f3691258172%22%7D; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; sessionid=rdb04hthtgwthsew1thgrc6c58t8uivl; gfsessionid=ew5dfw0yg6s930cpocalmz26rv110rzc; xm-page-viewid=ops-user-pilot-fe; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221859fede73d133e-0ad48ad2dced7d-17525635-2073600-1859fede73ed69%22%2C%22%24device_id%22%3A%221859fede73d133e-0ad48ad2dced7d-17525635-2073600-1859fede73ed69%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Falidocs.dingtalk.com%2F%22%2C%22%24latest_referrer_host%22%3A%22alidocs.dingtalk.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; sensorsdata2015session=%7B%7D; teambition_private_sid=eyJ1aWQiOiI2MzkxNDRjZmVjYzA0ZjM2OTEyNTgxNzIiLCJhdXRoVXBkYXRlZCI6MTY3MDQ2NDcxOTczMiwidXNlciI6eyJfaWQiOiI2MzkxNDRjZmVjYzA0ZjM2OTEyNTgxNzIiLCJuYW1lIjoi5byg5p+UIiwiZW1haWwiOiJyb3UuemhhbmdAeGltYWxheWEuY29tIiwiYXZhdGFyVXJsIjoiaHR0cHM6Ly90ZWFtYml0aW9uZmlsZS54aW1hbGF5YS5jb20vdGh1bWJuYWlsLzAxMm8zMTRhOWExMTY5Y2Y0MTYwZmJhMTI5MjBjY2ZiNmM4Ni93LzIwMC9oLzIwMCIsInJlZ2lvbiI6IiIsImxhbmciOiIiLCJpc1JvYm90IjpmYWxzZSwib3BlbklkIjoiIiwicGhvbmVGb3JMb2dpbiI6IiJ9LCJsb2dpbkZyb20iOiIifQ==; teambition_private_sid.sig=uwfHbDX1LpvHHqpV2YghNrbGMwU'
        # 0:不开通 1：开通
        isOpenlvb=request.json.get('isOpenlvb')
        ress={}
        for uid in uids:
        #     print(uid)
            # 实名认证(主播+v)
            url='http://ops.test.ximalaya.com/anchor-verify-backend/verify/quickAddVprofileVerify'
            # 随机更新身份证
            newidcard="511303"+str(random.randint(1980,2021))+"0"+str(random.randint(1,12))+str(random.randint(1,20))+"1981"
            body={
            "uid":uid,
            "uname": "anna",
            "gender": 1,
            "email": "12345678@163.com",
            "address": "再那遥远的地方",
            "vtype": 1,
            "phone": "16621325482",
            "realname": "测试认证",
            "cardtype":"二代身份证",
            "newidcard": newidcard,
            "idcardpath": "f7cafebd",
            "weiboinfo": "weibo",
            "birthday":"1995-07-15"
        }
            Referer='http://ops.test.ximalaya.com/anchor-verify-backend/index/userauth?tab=1'
            headers={"Accept":"application/json, text/plain, */*","Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8","Content-Type": "application/json","cookie":cookie}
            res=requests.post(url,data=json.dumps(body),headers=headers)
            if isOpenlvb==True:
                status = Openlv(uid)
                if res.json()['code']==4009 and status==True:
                    ress[uid]={'code':203,'msg':'用户已认证，视频直播权限开通成功'}
                elif res.json()['code']==4009 and status==False:
                    ress[uid] = {'code': 203, 'msg':  '用户已认证，视频直播权限开通失败'}
                elif res.json()['msg']=='请求成功' and status==True:
                    ress[uid]={'code':200,'msg':'用户实名认证+视频直播权限开通成功'}
                elif res.json()['msg']=='请求成功' and status==False:
                    ress[uid] = {'code': 203, 'msg': '用户实名认证成功，视频直播权限开通失败'}
            else:
                if res.json()['msg']=='请求成功' and isOpenlvb==False:
                    ress[uid] = {'code': 200, 'msg': '用户实名认证+视频直播权限开通成功'}
        return jsonify(ress)
        # return jsonify(res.json())
    except Exception as e:
        if res.text.find('认证中心'):
            res={"code":500,"msg":"cookie已过期，请@张柔"}
            return  jsonify(res)

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
@app.route('/Openlv',methods=['post'])
def Openlv(uid):
#     连接数据库
    database='lamia'
    sql1='select id from tb_live_room where uid=%d'%int(uid)
    # 表tb_live_room根据uid查到对应id
    roomid=Common.execute_sql(datas['host1'],datas['port1'],'lamia',datas['user'],datas['password'],sql1)[0]
    print('roomid是%d'%roomid)
    sql2='select * from tb_live_room_auth where room_id=%d'%int(roomid)
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
            return "success"
    else:
        return False
@app.route('/Openlv',methods=['post'])
def OpenGoods(uid):
    #连接数据库
    database = 'lamia'
    sql1 = 'select id from tb_live_room where uid=%d' % int(uid)
    # 表tb_live_room根据uid查到对应id
    roomid = Common.execute_sql(datas['host1'], datas['port1'], 'lamia', datas['user'], datas['password'], sql1)[0]
    print('roomid是%d' % roomid)
    sql2 = 'select * from tb_live_room_auth where room_id=%d' % int(roomid)
    df = Common.read_sql(datas['host1'], datas['port1'], 'lamia', datas['user'], datas['password'], sql2)
    # 判断用户是否已开通视频权限
    if df.empty:
        sql3 = "INSERT INTO tb_live_room_auth ( `room_id`, `type`, `start_at`, `end_at`, `deleted`, `created_at`, `updated_at`)" \
               "VALUES(%d, 2, now(), now(), 0, now(), now())" % int(roomid)
        res = Common.execute_sql(datas['host1'], datas['port1'], 'lamia', datas['user'], datas['password'], sql3)
        df = Common.read_sql(datas['host1'], datas['port1'], 'lamia', datas['user'], datas['password'], sql2)
        if df.empty:
            return False
        else:
            return True
    else:
        return False
# 用户侧实名
"""sql：
 INSERT INTO `tb_live_verify_user_info` (`uid`, `real_name`, `id_type`, `id_num`, `country_code`, `hold_id_img_store_id`, `birthdate`, `status`, `refuse_reason`, `verify_time`, `verify_type`, `created_at`, `updated_at`)
VALUES (1167510, 'S3oFPbFlPEGmXlPjwbcNfQ==', 1, 'ILFuXZ8epqRiZkr3kFwOsA10LTmEDm10zcwkn09St2Q=', NULL, NULL, '1996-10-05', 1, NULL, 1656841621732, 1, '2022-07-03 17:47:01', '2022-07-03 17:47:01');
#实人认证：1 二要素认证：1  年满18岁：1 用户认证：1
redis：set live_verify_user_cmp_1298182 15 """
@app.route('/AddCourselivewhitelist',methods=['post'])
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
                    print('失败')
                else:
                    print('成功')
            else:
                if da[0]==0:
                    print('已存在')
    except Exception as e:
        print(e)
# 开通卖货白名单
def open_goods(uids):
    uids = uids.split(',')
    database = 'diablo'
    try:
        for uid in uids:
            uid = int(uid)
            da = Common.execute_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'],
                                    "INSERT INTO tb_white_anchor_new('uid') VALUES(%d)"%(uid))
            # pd.set_option('display.max_columns', None)
            sub_categoryId = random.randint(100001, 100009)
            # 判断主播是否已开通权限
            if da == None:
                sql1 = "INSERT INTO tb_white_anchor (uid,apply_name,dept_name,reason,ops_id,created_at,updated_at,sub_categoryId,is_deleted,audit_director) " \
                       "VALUES(%d, 'autotest', '互娱', '加入白名单', 1,now(), now(), %d, 0, '张柔' )" % (
                       uid, sub_categoryId)
                da = Common.execute_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'],
                                        sql1)
                sql2 = 'SELECT * FROM tb_white_anchor where uid=%d' % (uid)
                df = Common.read_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'], sql2)
                # 断言
                if df.empty:
                    print('失败')
                else:
                    print('成功')
            else:
                if da[0] == 0:
                    print('已开通卖货权限')
    except Exception as e:
        print(e)
# 创建课程直播
@app.route('/Createcourselive',methods=['post'])
def Create_course_live():
    # 开通课程直播白名单
    uids=request.json.get('uid')
    # 开通课程直播白名单
    addCourselivewhitelist(uids)
    # 开通主播卖货白名单
    open_goods(uids)
    uids=uids.split(',')
    # 直播类型：测试、正式、付费
    coursetype=request.json.get('coursetype')
    # 直播开始时间，当时时间+min，如当前时间+20分钟为开始时间，那么填20
    Mtime=request.json.get('Mtime')
    Altime=request.json.get('Altime')
    price=request.json.get('price')
    # uids='1294839'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://192.168.3.54:8901',
        'Referer': 'http://192.168.3.54:8901/thriftTester/?iface=com.ximalaya.live.fans.club.api.thrift.TFansClubService$Iface&artifactId=live-fans-club-api&group=live-fans-club&scope=default&ip=172.26.6.141&port=2108&method=setRelationNoActive&reqParam=%7B%0A%20%20%22fansUid%22%3A%201244267%2C%0A%20%20%22anchorUid%22%3A%201155190%0A%7D',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    content=''
    # 默认付费类型
    isPaid="false"
    isTest="false"
    detailDescription = "http://audiotest.cos.tx.xmcdn.com/storages/6729-audiotest/1F/95/GKwaCHkHfw1CAAhAOwAAmwrL.jpeg"
    for uid in uids:
        timestamp=int(time.time())
        startime = timestamp - timestamp % (Mtime * 60) + (Mtime * 60)
        endtime = timestamp - timestamp % ((Mtime+Altime) * 60) + ((Mtime+Altime) * 60)
        if coursetype=='付费':
            isPaid = "true"
        if coursetype=='测试':
            isTest="true"
            detailDescription ="null"
        if coursetype == '正式':
            pass
        param={
        "input": {
            "roomId": 100001, #房间id
            "name": coursetype+"直播",
            "coverPath": "http://audiotest.cos.tx.xmcdn.com/storages/6729-audiotest/1F/95/GKwaCHkHfw1CAAhAOwAAmwrL.jpeg",
            "uid": uid,
            "description": "课程直播测试",
            "categoryId": 100101,
            "showPlayback": "false",
            "isAutoPull": "false",
            "non_recommended": "true",
            "isTest": isTest,
            "pushStreamType": 1,
            "openGoods": "true",
            "detailDescription": detailDescription,
            "isPaid": isPaid,
            "clearRate": 0,
            "price": price,
        }
    }
        # "{\\n\\"input\\": {\\n\\"roomId\\": 100001,\\n\\"name\\": \\"test\\",\\n\\"coverPath\\": \\"http://audiotest.cos.tx.xmcdn.com/storages/6729-audiotest/1F/95/GKwaCHkHfw1CAAhAOwAAmwrL.jpeg\\",\\n\\"uid\\": 1294839,\\n\\"startAt\\": 1673946600000,\\n\\"description\\": \\"张柔直播测试\\",\\n\\"endAt\\": 1673950200000,\\n\\"categoryId\\": 100101,\\n\\"showPlayback\\": \\"false\\",\\n\\"isAutoPull\\": \\"false\\",\\n\\"non_recommended\\": \\"true\\",\\n\\"isTest\\": \\"true\\",\\n\\"pushStreamType\\": 1,\\n\\"openGoods\\": \\"false\\",\\n\\"isPaid\\": \\"false\\",\\n \\"clearRate\\": 0\\n}\\n}"
        data = {
            'params': '{"group":"diablo-live","scope":"default","url":"","iface":"com.ximalaya.diablo.live.business.api.thrift.TDiabloLiveService$Iface","artifactId":"diablo-live-business-api","method":"createLive","authAapplication":"","isPeakReq":false,"params":%s}'%param,
        }
        re = requests.post('http://192.168.3.54:8901/thriftTester/v3/invoke.htm', headers=headers, data=data,verify=False)
    #     获取code的内容
        content=json.loads(re.text)['content']

    return jsonify(content)
    # return json.loads(content)
if __name__ == '__main__':
    from netifaces import interfaces, ifaddresses, AF_INET
    addresses = ''
    try:
        for name in interfaces():
            addresses = [i['addr'] for i in ifaddresses(name).setdefault(AF_INET, [{'addr': 'No IP '}])][0]
        app.run(host=addresses, port=8803, debug=False,threaded=True)
    except Exception:
        addresses = '127.0.0.1'
        app.run(host=addresses, port=8803, debug=False,threaded=True)
    # print(Certification())

