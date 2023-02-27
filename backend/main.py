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
    redirect_uri = request.args.get('redirect_uri')
    if redirect_uri is None or len(redirect_uri) == 0:
        HTTPException('redirect_uri 参数必传')
    else:
        try:
            return redirect(redirect_uri)
        except Exception as e:
            HTTPException('重定向[{}]失败'.format(redirect_uri), e)
            raise HTTPException('重定向[{}]失败！'.format(redirect_uri))
# 主播实名认证+开通视频&卖货权限
@app.route('/AddVprofileVerify',methods=['POST'])
def Certification():
    # data = json.loads(request.form.get('data'))
    data = json.loads(request.get_data())
    # print(request.form.get('data'))
    uids=data['uid']
    isOpenlvb=data['isOpenlvb']
    isOpengoods=data['isOpengoods']
    # uids=request.form.get('uid')
    # cookie=request.form.get('cookie')
    # isOpenlvb=request.form.get('isOpenlvb')
    # isOpengoods=request.form.get('isOpengoods')
    # uids = request.json.get('uid')
    # cookie = request.json.get('cookie')
    # True:不开通 False：开通
    # isOpenlvb = request.json.get('isOpenlvb')
    # isOpenGoods = request.json.get('isOpengoods')
    ress=certification(uids,isOpenlvb,isOpengoods)
    return jsonify(ress)
# 创建课程直播
@app.route('/CreatecourseLive',methods=['post'])
def Create_course_live():
    data = json.loads(request.get_data())
    uids=data['uid']
    # 直播类型：测试直播、正式直播、付费直播
    coursetype=data['coursetype']
    # 直播开始时间，当时时间+min
    Mtime=data['Mtime']
    Altime=data['Altime']
    price=data['price']
    ress=create_course_live(uids,coursetype,Mtime,Altime,price)
    return jsonify(ress)
if __name__ == '__main__':
    # 本地调试
    app.run(host='0.0.0.0', debug=False,threaded=True)
    # server=pywsgi.WSGIServer(('0.0.0.0',8000),app)
    # server.serve_forever()


