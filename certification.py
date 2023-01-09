import json,random,requests
import pymysql,pandas as pd,requests
from common import Common
from flask import Flask,jsonify,request
app = Flask(__name__)#创建一个服务，赋值给APP
#指定接口访问的路径，支持什么请求方式get，post讲的是封装成一种静态的接口，无任何参数传入

# uvicorn.run(app=app, host="localhost", port=8000, workers=1)
# 一键开通开播权限
# 实名认证
cookie='JSESSIONID=7C92A639E500B67FB0BFA837D8469BB9; _xmLog=h5&b3495f98-1f5e-4b27-82b1-1706b5bb0742&process.env.sdkVersion; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1670409250; teambition_lang=zh; TB_GTA=%7B%22pf%22%3A%7B%22cd%22%3A%22.ximalaya.com%22%2C%22dr%22%3A0%7D%2C%22uk%22%3A%22639144cfecc04f3691258172%22%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22184f4c81c78570-0c5bd360daadc9-17525635-1296000-184f4c81c79e4d%22%2C%22%24device_id%22%3A%22184f4c81c78570-0c5bd360daadc9-17525635-1296000-184f4c81c79e4d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sessionid=enrip9wxc144f3kqjeo2ufvj1ka1mf3g; koa:sess:live-admin-main=88d2f5ff-9ace-439a-a848-32a9da4d7778; koa:sess:live-admin-main.sig=sDDocN3ZbFlE71HXLKVv5VsFZ2I; 4&remember_me=y; 4&_token=57557&45F720C0240N6E505A9D534DB5ED2A0527397192A745DB219B3678E9899A7B06D868AC25A00D58MB3BFAFFD151A2AF_; login_type=password_mobile; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; _const_cas_ticket=48806472a202493ca56050a20bb7180a'
def Request(param):
    param=request.json.get(param)
    return param
# @app.route('/AddVprofileVerify',methods=['post'])

def Certification(uid,cookie=cookie):
    # uid = request.json.get('uid')
    # phone = request.json.get('phone')

    # 实名认证(主播+v)
    url='http://ops.test.ximalaya.com/anchor-verify-backend/verify/quickAddVprofileVerify'
    # 随机更新身份证
    newidcard="220282"+str(random.randint(1700,2022))+"01230187"
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
    response=requests.post(url,data=json.dumps(body),headers=headers)
    print(response.json())
    return response.json()
    # pd.set_option('display.max_columns', None)
    # 开通视频直播权限
def addCourselivewhitelist():
    uid=1294839
    host = '192.168.60.11'
    database = 'diablo'
    # 课程直播白名单添加
    try:
        da = Common.execute_sql(host, database, 'select is_deleted from tb_white_anchor where uid=%d' % (uid))
        # pd.set_option('display.max_columns', None)
        # 判断主播是否已开通权限
        sub_categoryId=random.randint(100001,100009)
        if da==None:
            da = Common.execute_sql(host, database,"INSERT INTO tb_white_anchor (uid,apply_name,dept_name,reason,ops_id,created_at,updated_at,sub_categoryId,is_deleted,audit_director) "
                           "VALUES(%d, 'autotest', '互娱', '加入白名单', 1,now(), now(), %d, 0, '张柔' )"%(uid,sub_categoryId))
            df = Common.read_sql(host, database,'SELECT * FROM tb_white_anchor where uid=%d' % (uid))
            # 断言
            if df.empty:
                res={'code':400,'result':'用户{}开播权限开通失败，请重试！'.format(uid)}
            else:
                res={'code':200,'result':'用户{}开播权限开通成功！'.format(uid)}
        else:
            if da[0]==0:
                res={'code':200,'result':'用户{}已开通开播权限'.format(uid)}
            else:
                res={'code':200,'result':'用户{}权限已被关闭'.format(uid)}
        print(res)
        # return jsonify(res)
    except Exception as e:
        print(e)
        # return jsonify(e)

# 添加主播卖货权限
# @app.route('/AddSellgoods',methods=['post'])
def add_sell_goods():
    pass
# @app.route('/CreateCourseLive',methods=['post'])
def Create_course_live():

    url='http://ops.test.ximalaya.com/diablo-admin/v1/record/create'
    # coursetype = request.json.get('coursetype')
    uid ="1297286"
    coursetype=input('请输入课程直播类型')
    # uid=request.json.get('uid')
    # 声明变量
    global clearRate,isTest,isPaid,openGoods
    # clearRate=50
    # isTest = True
    # isPaid=False
    # try:
    if coursetype == '测试直播':
        clearRate = " "
        isTest = True
        isPaid=False
        openGoods = False
    elif coursetype == '正式直播':
        isTest=False
        openGoods = True
    elif coursetype == '付费直播':
        #分成比例
        clearRate=request.json.get('clearRate')
        # 是否开启卖货功能
        openGoods=request.json.get('openGoods')
    body={"uid": "1297286","adminUids": [],"name": "张柔_测试","coverPath": "http://audiotest.cos.tx.xmcdn.com/storages/6729-audiotest/1F/95/GKwaCHkHfw1CAAhAOwAAmwrL.jpeg",' \
         '"description": "付费直播测试","topicTagId": -1,"pushStreamType": 1,"screenSize": True,"isTest": True,"notifyFans": False,' \
         '"showPlayBack": False,"nonRecommended": True,"openGoods": openGoods,"openGift": True,"forbidSpeak": False,"isPaid":True,' \
         '"detailDescription": "http://audiotest.cos.tx.xmcdn.com/storages/8dba-audiotest/99/E1/GKwaCHkHgdbiAACHywAAmygz.jpg","isAutoPull": False,"categoryId": 100101,"startAt": None,"endAt": None,"price": "10","clearRate": clearRate}

    Origin='http: // ops.test.ximalaya.com'
    Referer='http://ops.test.ximalaya.com/diablo-admin/index/liveScene?pageId=1&pageSize=20'
    headers={"Accept":"application/json, text/plain, */*","Accept-Language": "zh-CN,zh;q=0.9","Content-Type": "application/json","cookie":cookie,"Referer":Referer,"Origin":Origin}
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response.text
    # except Exception as e:
    #     print(e)

if __name__ == '__main__':
    # 获取本机ip地址
    # from netifaces import interfaces, ifaddresses, AF_INET
    # addresses = ''
    # for name in interfaces():
    #     addresses = [i['addr'] for i in ifaddresses(name).setdefault(AF_INET, [{'addr': 'No IP '}])]
    # print('demo ran in host:%s'%(addresses[0]))
    # app.run(host=addresses[0], port=8802, debug=False)
    # open_ringhts()
    # uids=1297286,1297362,1297498,1297499
    # for uid in uids:
    #     Certification(uid)
    # print(Create_course_live())
    addCourselivewhitelist()
