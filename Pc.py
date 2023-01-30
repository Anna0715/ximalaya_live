import random,requests,json,time
from flask import Flask,jsonify,request,Blueprint
from common import Common
Pc=Blueprint('Pc',__name__)
app = Flask(__name__)#创建一个服务，赋值给APP
datas=Common.get_data()
# 添加课程直播白名单
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
                    print('已存在')
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
    # 直播开始时间，当时时间+min
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
    # print(addCourselivewhitelist('1288819,1298487,1298488,1298489'))
    from netifaces import interfaces, ifaddresses, AF_INET
    addresses = ''
    try:
        for name in interfaces():
            addresses = [i['addr'] for i in ifaddresses(name).setdefault(AF_INET, [{'addr': 'No IP '}])][0]
        app.run(host=addresses, port=8803, debug=False)
    except Exception:
        addresses = '127.0.0.1'
        app.run(host=addresses, port=8803, debug=False)
    # print(Create_course_live())