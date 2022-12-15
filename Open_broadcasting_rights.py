import pymysql,pandas as pd
from flask import Flask,jsonify,request
app = Flask(__name__)#创建一个服务，赋值给APP
#指定接口访问的路径，支持什么请求方式get，post讲的是封装成一种静态的接口，无任何参数传入
@app.route('/open_ringhts',methods=['post'])
# uvicorn.run(app=app, host="localhost", port=8000, workers=1)
# 一键开通开播权限
def open_ringhts():
    try:
        uid =request.json.get('uid')
        conn = pymysql.connect(
            user='naliworld',  # 用户名
            password='password!',  # 密码：这里一定要注意123456是字符串形式
            host='192.168.60.11',  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
            database='diablo',  # 数据库的名字
            port=3306,  # 指定端口号，范围在0-65535
            charset='utf8',  # 数据库的编码方式
        )
        # while True:
        #     uid=input('请输入uid：')
        #     if uid.isdigit():
        #         uid=int(uid)
        #         break
        #     else:
        #         print('请输入正确的uid')
        cursor = conn.cursor()
        # pd.set_option('display.max_columns', None)
        cursor.execute('select is_deleted from tb_white_anchor where uid=%d'%(uid))
        da=cursor.fetchone()
        # 判断主播是否已开通权限
        if da==None:
            cursor.execute("INSERT INTO tb_white_anchor (uid,apply_name,dept_name,reason,ops_id,created_at,updated_at,sub_categoryId,is_deleted,audit_director) "
                           "VALUES(%d, 'autotest', '互娱', '加入白名单', 1,now(), now(), 1007, 0, '张柔' )"%(uid))
            # 关闭当前游标
            cursor.close()
            conn.commit()  # 提交事务，必须要执行，否则数据不会被真正插入
            df = pd.read_sql('SELECT * FROM tb_white_anchor where uid=%d' % (uid), con=conn)
            # 断言
            if df.empty:
                res={'code':400,'result':'用户{}开播权限开通失败，请重试！'.format(uid)}
            else:
                res={'code':200,'result':'用户{}开播权限开通成功！'.format(uid)}
            conn.close()  # 关闭数据库连接
        else:
            if da[0]==0:
                res={'code':200,'result':'用户{}已开通开播权限'.format(uid)}
            else:
                res={'code':200,'result':'用户{}权限已被关闭'.format(uid)}
        return jsonify(res)
    except Exception as e:
        return jsonify(e)
def  Certification():
    pass
if __name__ == '__main__':
    # 获取本机ip地址
    from netifaces import interfaces, ifaddresses, AF_INET
    addresses = ''
    for name in interfaces():
        addresses = [i['addr'] for i in ifaddresses(name).setdefault(AF_INET, [{'addr': 'No IP '}])]
    print('demo ran in host:%s'%(addresses[0]))
    app.run(host=addresses[0], port=8802, debug=False)
    # open_ringhts()
