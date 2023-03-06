from http.client import HTTPException
from flask import Flask, jsonify, request, render_template, redirect
from client import *
from Pc import *
from flask_cors import *
from gevent import pywsgi
app = Flask(__name__,
            template_folder="../frontend/dist",
            static_folder="../frontend/dist",
            static_url_path="")#创建一个服务，赋值给APP
CORS(app,supports_credentials=True)
datas=Common.get_data()
@app.route("/")
@app.route("/user/login")
@app.route("/consumer/certification")
def index():
    return render_template('index.html')

# 登陆接口
@app.route('/login', methods=['GET'])
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
@app.route('/AddVprofileVerify',methods=['POST'])
def Certification():
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
@app.route('/CreateCourseLive',methods=['post'])
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
    price=data['price']
    quantity=data['quantity']
    clearRate = data['clearRate']
    ress=create_course_live(uids,coursetype,openGoods,openGift,showPlayback,startAt,endAt,price,quantity,clearRate)
    return jsonify(ress)
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80,debug=False,threaded=True)
    server=pywsgi.WSGIServer(('0.0.0.0',80),app)
    server.serve_forever()


