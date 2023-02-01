import json,random,requests
from common import Common
datas=Common.get_data()
# 主播实名认证
def certification(uids,cookie,isOpenlvb,isOpenGoods):
    global res
    try:
        ress={}
        data=[]
        for uid in uids:
            uid=int(uid)
            di={}
            if isOpenlvb == True:
                openlvb_status = Openlv(uid)
                di['Openlv']=openlvb_status
            if isOpenGoods == True:
                opengoods_status =open_goods(uid)
                di["OpenGoods"]=opengoods_status
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
            # 返回的响应请求结果生成键值对添加到data中
            if res.json()['msg']=='请求成功' or res.json()['msg']==4009:
                di["profileVerify"]= True
            if (di["profileVerify"]==True or di["profileVerify"]=="success") and di['Openlv']=="success" and di["OpenGoods"]=="success":
                di["code"]=200
            if di["profileVerify"] == True and(di['Openlv'] == "fail" or di["OpenGoods"] == "fail"):
                di["code"] = 203
            data.append(di)
            # 构造字典格式的返回响应
            ress["data"]=data
            ress["msg"]="请求成功"
        return ress
        # return jsonify(res.json())
    except Exception as e:
        if res.text.find('认证中心'):
            ress={"code":500,"data":[],"msg":"cookie已过期，请@张柔"}
            return  ress

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
# 开通视频权限
def Openlv(uid):
#     连接数据库
    database='lamia'
    sql1='select id from tb_live_room where uid=%d'%int(uid)
    # 表tb_live_room根据uid查到对应id
    roomid=Common.execute_sql(datas['host1'],datas['port1'],'lamia',datas['user'],datas['password'],sql1)[0]
    print(type(uid),type(roomid))
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
    # 用户已开通视频权限直接返回
    else:
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
            print(da)
            # 判断主播是否已开通权限
            if da == None:
                sql = "INSERT INTO tb_white_anchor_new (uid) values(%d)"%(uid)
                da = Common.execute_sql(datas['host1'], datas['port1'], database, datas['user'], datas['password'],
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
        return e
if __name__ == '__main__':
    pass