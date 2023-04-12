from http.client import HTTPException
from flask import Flask, jsonify, request, render_template, redirect, make_response
from client import *
from Pc import *
from flask_cors import *
from gevent import pywsgi
# from logging.config import dictConfig
# dictConfig({
#         "version": 1,
#         "disable_existing_loggers": False,  # 不覆盖默认配置
#         "formatters": {  # 日志输出样式
#             "default": {
#                 "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#             }
#         },
#         "handlers": {
#             "console": {
#                 "class": "logging.StreamHandler",  # 控制台输出
#                 "level": "DEBUG",
#                 "formatter": "default",
#             },
#             "log_file": {
#                 "class": "logging.handlers.RotatingFileHandler",
#                 "level": "INFO",
#                 "formatter": "default",   # 日志输出样式对应formatters
#                 "filename": "./logs/flask.log",  # 指定log文件目录
#                 "maxBytes": 20*1024*1024,   # 文件最大20M
#                 "backupCount": 10,          # 最多10个文件
#                 "encoding": "utf8",         # 文件编码
#             },
#
#         },
#         "root": {
#             "level": "DEBUG",  # # handler中的level会覆盖掉这里的level
#             "handlers": ["console", "log_file"],
#         },
#     }
# )

app = Flask(__name__,
            template_folder="./templates",
            static_folder="./templates",
            static_url_path="")#创建一个服务，赋值给APP
app.config['JSON_AS_ASCII'] = False
CORS(app,supports_credentials=True)
datas=Common.get_data()
# XDCS健康检查端口
@app.route("/ximalive-qa/healthcheck",methods=['GET'])
def healthcheck():
    response=make_response('* xdcs.default.healthCheck: OK\nhealthCheck success')
    return response
@app.route("/ximalive-qa/")
def index():
    return render_template('index.html')

# 登陆接口
@app.route('/ximalive-qa/login', methods=['GET'])
def login():
    redirect_url = request.args.get('redirect_url')
    if redirect_url is None or len(redirect_url) == 0:
        HTTPException('redirect_url 参数必传')
    else:
        try:
            return redirect(redirect_url)
        except Exception as e:
            HTTPException('重定向[{}]失败'.format(redirect_url), e)
            raise HTTPException('重定向[{}]失败！'.format(redirect_url))
# 主播实名认证+开通视频&卖货权限
@app.route('/ximalive-qa/AddVprofileVerify',methods=['POST'])
def Certification():
    # app.logger.debug(f'login request payload: {request.get_data()}')
    data = json.loads(request.get_data())
    uids = data['uid']
    isOpenlvb = data['isOpenlvb']
    isOpengoods = data['isOpengoods']
    print(isOpenlvb)
    if isOpenlvb==" ":
        isOpenlvb=False
    if isOpengoods==" ":
        isOpengoods=False
    # uids = request.json.get('uid')
    # True:不开通 False：开通
    # isOpenlvb = request.json.get('isOpenlvb')
    # isOpengoods = request.json.get('isOpengoods')
    ress=certification(uids,isOpenlvb,isOpengoods)
    return jsonify(ress)
# 创建课程直播
@app.route('/ximalive-qa/CreateCourseLive',methods=['post'])
def Create_Course_live():
    data = json.loads(request.get_data())
    uids=data['uid']
    # 直播类型：测试、正式、付费
    coursetype=data['coursetype']
    openGoods = data['openGoods']
    openGift = data['openGift']
    showPlayback=data['showPlayback']
    try:
        startAt=data['startAt']
        endAt = data['endAt']
    except:
        startAt = (datetime.datetime.now() + datetime.timedelta(minutes=20)).strftime("%Y-%m-%d %H:%M:%S")
        endAt = (datetime.datetime.now() + datetime.timedelta(minutes=50)).strftime("%Y-%m-%d %H:%M:%S")
    # 由于平台侧的时间有延迟所以
    price=data['price']
    quantity=data['quantity']
    clearRate = data['clearRate']
    ress=create_course_live(uids,coursetype,openGoods,openGift,showPlayback,startAt,endAt,price,quantity,clearRate)
    return jsonify(ress)
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=7169,debug=False,threaded=True)
    server=pywsgi.WSGIServer(('0.0.0.0',7169),app)
    server.serve_forever()


