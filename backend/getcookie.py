import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests,json,os,time
import sys
import time
from lxml import etree
# reload(sys)
# sys.setdefaultencoding('utf-8')

class get_cookie:
    loginurl='http://ops.test.ximalaya.com/cas-server/login?'
    homeurl = loginurl+'service=http%3A%2F%2Fops.test.ximalaya.com%2Flive-admin-main'
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
        options=Options()
        options.add_argument('headless')
        # browser = webdriver.Chrome(executable_path='/Users/rou.zhang/Desktop/ximalaya_live/tool/chromedriver',options=options)
        browser = webdriver.Chrome('/Users/rou.zhang/Desktop/ximalaya_live/backend/tool/chromedriver')
        browser.get(self.homeurl)
        # browser.get("http://ops.test.ximalaya.com/live-admin-main/operationPosition?pageId=1&pageSize=20&name=%E5%8D%AF%E5%85%94")
        # 输入账号
        browser.find_element_by_xpath("//input[@id='username']").send_keys("rou.zhang")
        # 输入密码
        browser.find_element_by_xpath("//input[@id='password']").send_keys("anna1995@")
        time.sleep(5)
        # 点击登录
        browser.find_element_by_xpath("//button[@name='submit']").click()
        time.sleep(5)
        js='document.cookie'
        cookies=browser.execute_script(js)
        # cookies = browser.get_cookies()
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
        time.sleep(4)
        s = requests.session()
        Cookies = {
            'org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE': 'zh_CN',
            'gfsessionid': 'exjcf901vh11o8cq6wxzktpjli1g03bc',
            '_audit_cas_ticket': 'ST-50605-wXBOnwompFezqWKZQIyw-ops.ximalaya_node1.com',
            '_const_cas_ticket': '4b9c0de57d1f492cb02c64a357e264c0',
            'sessionid': 'qso7hp3r5vz289hkqc5440hzlufiprb3',
            'teambition_lang': 'zh',
            'TB_GTA': '%7B%22pf%22%3A%7B%22cd%22%3A%22.ximalaya.com%22%2C%22dr%22%3A0%7D%2C%22uk%22%3A%22639144cfecc04f3691258172%22%7D',
            '_xmLog': 'h5&7ebc0275-7c9c-48cd-8999-ef3d5cbfe4af&2.4.6',
            'teambition_private_sid': 'eyJ1aWQiOiI2MzkxNDRjZmVjYzA0ZjM2OTEyNTgxNzIiLCJhdXRoVXBkYXRlZCI6MTY3MDQ2NDcxOTczMiwidXNlciI6eyJfaWQiOiI2MzkxNDRjZmVjYzA0ZjM2OTEyNTgxNzIiLCJuYW1lIjoi5byg5p+UIiwiZW1haWwiOiJyb3UuemhhbmdAeGltYWxheWEuY29tIiwiYXZhdGFyVXJsIjoiaHR0cHM6Ly90ZWFtYml0aW9uZmlsZS54aW1hbGF5YS5jb20vdGh1bWJuYWlsLzAxMm8zMTRhOWExMTY5Y2Y0MTYwZmJhMTI5MjBjY2ZiNmM4Ni93LzIwMC9oLzIwMCIsInJlZ2lvbiI6IiIsImxhbmciOiIiLCJpc1JvYm90IjpmYWxzZSwib3BlbklkIjoiIiwicGhvbmVGb3JMb2dpbiI6IiJ9LCJsb2dpbkZyb20iOiIifQ==',
            'teambition_private_sid.sig': 'uwfHbDX1LpvHHqpV2YghNrbGMwU',
            'koa:sess:live-admin-main': 'bc71b27b-3612-4682-8000-3ccd5cd860bf',
            'koa:sess:live-admin-main.sig': 'x4InZfSkKtVMgwpliYtxZn-pGMQ',
            'xm-page-viewid': 'ops-anchor-center',
            'trackType': 'web',
            'x_xmly_traffic': 'utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A',
            'impl': 'passport.ximalaya.com.web',
        }
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': Cookie,
            'Referer': 'http://ops.test.ximalaya.com/live-admin-main',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        resp = s.get(
            'http://ops.test.ximalaya.com/live-admin-main/api/getMenuList',
            cookies=Cookies,
            headers=headers,
            verify=False,
        )
        print(resp.cookies)
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