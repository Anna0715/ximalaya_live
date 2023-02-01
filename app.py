from flask import Flask,jsonify,request
from client import *
from Pc import *
from gevent import pywsgi
app = Flask(__name__)#创建一个服务，赋值给APP
datas=Common.get_data()
@app.route("/")
def index():
    return "annatest!!"
# 主播实名认证+开通视频&卖货权限
@app.route('/AddVprofileVerify',methods=['post'])
def Certification():
    uids = request.json.get('uid').split(',')
    cookie = request.json.get('cookie')
    # cookie='JSESSIONID=6670122F057E726BD6AAEA8895FF58D8; _xmLog=h5&627809bd-3ca9-46da-8136-f49845b87900&process.env.sdkVersion; teambition_lang=zh; TB_GTA=%7B%22pf%22%3A%7B%22cd%22%3A%22.ximalaya.com%22%2C%22dr%22%3A0%7D%2C%22uk%22%3A%22639144cfecc04f3691258172%22%7D; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; sessionid=rdb04hthtgwthsew1thgrc6c58t8uivl; gfsessionid=ew5dfw0yg6s930cpocalmz26rv110rzc; xm-page-viewid=ops-user-pilot-fe; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221859fede73d133e-0ad48ad2dced7d-17525635-2073600-1859fede73ed69%22%2C%22%24device_id%22%3A%221859fede73d133e-0ad48ad2dced7d-17525635-2073600-1859fede73ed69%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Falidocs.dingtalk.com%2F%22%2C%22%24latest_referrer_host%22%3A%22alidocs.dingtalk.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; sensorsdata2015session=%7B%7D; teambition_private_sid=eyJ1aWQiOiI2MzkxNDRjZmVjYzA0ZjM2OTEyNTgxNzIiLCJhdXRoVXBkYXRlZCI6MTY3MDQ2NDcxOTczMiwidXNlciI6eyJfaWQiOiI2MzkxNDRjZmVjYzA0ZjM2OTEyNTgxNzIiLCJuYW1lIjoi5byg5p+UIiwiZW1haWwiOiJyb3UuemhhbmdAeGltYWxheWEuY29tIiwiYXZhdGFyVXJsIjoiaHR0cHM6Ly90ZWFtYml0aW9uZmlsZS54aW1hbGF5YS5jb20vdGh1bWJuYWlsLzAxMm8zMTRhOWExMTY5Y2Y0MTYwZmJhMTI5MjBjY2ZiNmM4Ni93LzIwMC9oLzIwMCIsInJlZ2lvbiI6IiIsImxhbmciOiIiLCJpc1JvYm90IjpmYWxzZSwib3BlbklkIjoiIiwicGhvbmVGb3JMb2dpbiI6IiJ9LCJsb2dpbkZyb20iOiIifQ==; teambition_private_sid.sig=uwfHbDX1LpvHHqpV2YghNrbGMwU'
    # 0:不开通 1：开通
    isOpenlvb = request.json.get('isOpenlvb')
    isOpenGoods = request.json.get('isOpenGoods')
    ress=certification(uids,cookie,isOpenlvb,isOpenGoods)
    return jsonify(ress)
# 创建课程直播
@app.route('/Createcourselive',methods=['post'])
def Create_course_live():
    uids=request.json.get('uid')
    # 直播类型：测试直播、正式直播、付费直播
    coursetype=request.json.get('coursetype')
    # 直播开始时间，当时时间+min
    Mtime=request.json.get('Mtime')
    Altime=request.json.get('Altime')
    price=request.json.get('price')
    ress=create_course_live(uids,coursetype,Mtime,Altime,price)
    return jsonify(ress)
if __name__ == '__main__':
    from netifaces import interfaces, ifaddresses, AF_INET
    addresses = ''
    try:
        for name in interfaces():
            addresses = [i['addr'] for i in ifaddresses(name).setdefault(AF_INET, [{'addr': 'No IP '}])][0]
        app.run(host='0.0.0.0', port=7169, debug=False,threaded=True)
    except Exception:
        addresses = '127.0.0.1'
        app.run(host='0.0.0.0', port=7169, debug=False,threaded=True)


