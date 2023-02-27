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
def create_course_live(uids,coursetype,Mtime,Altime,price):
    # 开通课程直播白名单
    addCourselivewhitelist(uids)
    # 开通主播卖货白名单
    open_goods(uids)
    uids=uids.split(',')
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
    clearRate=0
    detailDescription = "http://audiotest.cos.tx.xmcdn.com/storages/6729-audiotest/1F/95/GKwaCHkHfw1CAAhAOwAAmwrL.jpeg"
    for uid in uids:
        m=(datetime.datetime.now()+datetime.timedelta(minutes=Mtime)).strftime("%Y-%m-%d %H:%M:%S")
        e=(datetime.datetime.now()+datetime.timedelta(minutes=Mtime+Altime)).strftime("%Y-%m-%d %H:%M:%S")
        startime=int(round(time.mktime(time.strptime(m,'%Y-%m-%d %H:%M:%S'))*1000))
        endtime = int(round(time.mktime(time.strptime(e,'%Y-%m-%d %H:%M:%S'))*1000))
        if coursetype=="付费直播":
            isPaid = "true"
            clearRate=50
        if coursetype=="测试直播":
            isTest="true"
            detailDescription ="null"
        if coursetype == '正式直播':
            pass
        param={
        "input": {
            "roomId": 100001, #房间id
            "name": coursetype,
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
            "clearRate":clearRate,
            "price": price,
            "startAt":startime,
            "endAt":endtime
        }
    }
        # "{\\n\\"input\\": {\\n\\"roomId\\": 100001,\\n\\"name\\": \\"test\\",\\n\\"coverPath\\": \\"http://audiotest.cos.tx.xmcdn.com/storages/6729-audiotest/1F/95/GKwaCHkHfw1CAAhAOwAAmwrL.jpeg\\",\\n\\"uid\\": 1294839,\\n\\"startAt\\": 1673946600000,\\n\\"description\\": \\"张柔直播测试\\",\\n\\"endAt\\": 1673950200000,\\n\\"categoryId\\": 100101,\\n\\"showPlayback\\": \\"false\\",\\n\\"isAutoPull\\": \\"false\\",\\n\\"non_recommended\\": \\"true\\",\\n\\"isTest\\": \\"true\\",\\n\\"pushStreamType\\": 1,\\n\\"openGoods\\": \\"false\\",\\n\\"isPaid\\": \\"false\\",\\n \\"clearRate\\": 0\\n}\\n}"
        data = {
            'params': '{"group":"diablo-live","scope":"default","url":"","iface":"com.ximalaya.diablo.live.business.api.thrift.TDiabloLiveService$Iface","artifactId":"diablo-live-business-api","method":"createLive","authAapplication":"","isPeakReq":false,"params":%s}'%param,
        }
        print(param)
        re = requests.post('http://192.168.3.54:8901/thriftTester/v3/invoke.htm', headers=headers, data=data,verify=False)
    #     获取code的内容
        content=json.loads(re.text)['content']
    return content
    # return json.loads(content)
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
"""
"""
def create_family_account():
    # 提交入驻资料申请
    sql1="INSERT INTO `tb_family_enter_apply_info` (`uid`, `warrent_person_info_id`, `company_id`, `family_info_id`, `contract_id`, `anchor_verify_center_status`, `verify_center_status`, `status`, `warrent_person_info_status`, `company_info_status`, `family_info_status`, `ops_id`, `operator`, `verify_refuse_reason`, `filed_time`, `created_at`, `updated_at`, `operator_ops_id`, `request_enterprise_reg_fail_msg`, `anchor_verify_center_update_time`) " \
        "VALUES (1304049, 252, 237, 185, NULL, 0, 0, 205, 1, 1, 1, NULL, NULL, NULL, NULL, now(), now(), NULL, NULL, NULL)"
    da = Common.execute_sql(datas['host1'], datas['port1'], 'lamia', datas['user'], datas['password'], sql1)
if __name__ == '__main__':
    pass