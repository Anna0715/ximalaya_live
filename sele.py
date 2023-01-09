import random
from certification import Certification
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests,json,os,time
import sys
import time
from lxml import etree

# reload(sys)
# sys.setdefaultencoding('utf-8')

class get_cookie:
    def __init__(self):
        self.homeurl = 'http://ops.test.ximalaya.com/cas-server/login'
    def save_session(self, session):  # 保存session，下次可直接使用，避免再次登录
        with open('session.txt', 'wb') as f:
            json.dump(session, f)
            print("Cookies have been writed.")

    def load_session(self):  # 加载session
        with open('session.txt', 'rb') as f:
            s = json.load(f)
        return s


    @classmethod
    def GetCookies(self):  # 初次登录用selenium模拟，并获得cookies


        # options=Options()
        # options.add_argument('headless')
        # browser = webdriver.Chrome(executable_path='/Users/rou.zhang/Desktop/ximalaya_live/tool/chromedriver',options=options)
        browser = webdriver.Chrome('/Users/rou.zhang/Desktop/ximalaya_live/tool/chromedriver')
        # browser.get("http://ops.test.ximalaya.com/cas-server/login")
        browser.get("http://ops.test.ximalaya.com/live-admin-main/operationPosition?pageId=1&pageSize=20&name=%E5%8D%AF%E5%85%94")
        # 输入账号
        browser.find_element_by_xpath("//input[@id='username']").send_keys("rou.zhang")
        # 输入密码
        browser.find_element_by_xpath("//input[@id='password']").send_keys("anna1995@")
        time.sleep(5)
        # 点击登录
        browser.find_element_by_xpath("//button[@name='submit']").click()
        time.sleep(10)

        cookies = browser.get_cookies()
        print(cookies)
        # 定义一个存储cookie的字符
        Cookie=''
        for i in cookies:
            if i['name']=='JSESSIONID':
                Cookie =Cookie+'JSESSIONID='+i['value']+';'
            elif i['name']=='_xmLog' :
                Cookie = Cookie + '_xmLog' + i['value'] + ';'
            elif i['name']=='sessionid' :
                Cookie = Cookie + 'sessionid' + i['value'] + ';'
            elif i['name']=='_audit_cas_ticket':
                Cookie = Cookie + '_audit_cas_ticket' + i['value'] + ';'
            elif i['name']=='_const_cas_ticket' :
                Cookie = Cookie + '_const_cas_ticket' + i['value']
        time.sleep(2000)
        # cookie拼接格式
        # TGC=;JSESSIONID=；_xmLog=；TB_GTA=；sessionid=；_audit_cas_ticket；_const_cas_ticket=
        browser.quit()
        return Cookie
if __name__ == '__main__':
    print(get_cookie.GetCookies())
    # try:
    #     Certification(1294839)
    # except Exception as e:
    #     print(e)
    #     cookie=get_cookie.GetCookies()
    #     Certification(1294839,cookie=cookie)
