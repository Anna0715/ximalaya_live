# 获取本机ip地址
from flask import Flask,jsonify,request
from netifaces import interfaces, ifaddresses, AF_INET
from Browser import app
addresses=''
try:
    for name in interfaces():
        addresses = [i['addr'] for i in ifaddresses(name).setdefault(AF_INET, [{'addr': 'No IP '}])][0]
    app.run(host=addresses, port=8803, debug=False)
except Exception:
    addresses = '127.0.0.1'
    app.run(host=addresses, port=8803, debug=False)