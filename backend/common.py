import pymysql,pandas as pd,requests,re,json,yaml,os

class Common:
    @classmethod
    def Conn(cls,host,port,database,user,password):
        conn = pymysql.connect(
            user=user,  # 用户名
            password=password,  # 密码：这里一定要注意123456是字符串形式
            host=host,  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
            database=database,  # 数据库的名字
            port=port,  # 指定端口号，范围在0-65535
            charset='utf8',  # 数据库的编码方式
        )
        return conn
    @classmethod
    def execute_sql(cls,host,port,user,password,database,sql):
        conn=cls.Conn(host,port,user,password,database)
        cursor = conn.cursor()
        cursor.execute(sql)
        da=cursor.fetchone()
        #关闭游标
        cursor.close()
        #提交事务
        conn.commit()
        return da
    @classmethod
    def read_sql(self,host,port,user,password,database,sql):
        conn=self.Conn(host,port,user,password,database)
        df = pd.read_sql(sql,con=conn)
        return df

    @classmethod
    def getCookie(self):
        s = requests.session()
        url = 'http://ops.test.ximalaya.com/cas-server/login'
        body = {"username": "rou.zhang", "password": "627873e8b7b0061ba2b2781b78cafbd2",
                "lt": "LT-78128-JQgbn0tqPNxUqVVcmTpVzrzt1cztXn-ops.ximalaya_node1.com",
                "execution": "e5e44378-4079-418d-890b-8ce4f0017331_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuYVZWS1oxRnpMeTlpUkVScWFFcEZXSHBWYTJZclJETnhlVE00TTFkNE1XTnFVRkEwT0VsU1RqaEtORzU1TUZKcFJtNVdUM1pDV1haRWEwWldSMFIyWmtKS1V6SnZla1JQYkRaelMyazVNWGxVVDAxTmFteEJjVEZhZWpCVlltbEVXR1JHYkhodWRVaG9ZVU42UlV0VlNrOW9NM0JFV2tKS0wwUllXVVZRUkZWdVpqbFBWa3R6YW1SUmFqWkdaR2wxTURkMWRVRk1SblZWVlV0eFFWUnZhM295Vm5ONVQyRlRXWE5sYkhCa1pFWjNialZ3TWpKWVNsTjNUMmRuYnpseWRuQTNWVk5ZZVdoS1UzcFBTalZJYlhZdlJHVjZhbWRWVVZscGVXcHhSa1Z3VVRCTWJEbEtjazF2TWtoWlpsWk5RMFIyUzFaNksySktkR0prSzI5T2FIcDJjSGt5V2pGeFUxbFhiRU5YZG5ncmNHdFdUV05MWjFJNFUyNTNhR1ZUUkVSUlprOUxhbFpzYjJaYVdVcHRLM0pvUVd4S2NuVXlSbUl5UmxCaFNrUktORzA0UkV3MmVFeGhVRkZCUjNscFJsZHBlakZDUjNoVk0yZ3hNSFl4VEhoV1FVOWhZVVpEVlVoNmJGVm9NbkIyVmtJdmJGaGxUVXc1T0d4UVIwVXhRbkEwUW5kTE1YRm9TR0YyUjB0WGIwVXJhMVJrTkdodldHOW9kRnBpZVhoaE5FVmxhaXMyVUhJeVZFbDVVRUZ1WTNaNmRGZHJOWG95WTNJdlJFZFFSSGNyTTFCV1UwMXpUWEV3WWxWclNERkhiVzFEYjNGeFpsSnJSRU5KU0VWd1JWSkNRVGxtVUhZNGNFaExkRGhOVEdVd2JDOTJlakpVV1hBelMwVldjVTlRTTFORlpqSmtkemRhUVVKRFkxZHZUMnQ0VWpKMlRUWk9hbVJETkRFMmIxUlFXQ3NyTjJWRmVVUmlaRUZpVlZFcmJWTmpTV3BpVXl0S1NWVm5TVU5yUzFwQk0wcE5UMUJ5VjNKM2FIWjFSV0Y1Y201S1ZEQnJVa2wyWW1wTFZFTkphMGRXVDBacU1IZFBVekpRVUdGRlZVRlFXRVZFTVU5bVkySkpNVGRMVVVwak1GaFZNMDF2UkV4NWJVOU5jR2hhSzNSeFZTczRjMnRMYVdOclJYTk5PV3QxTm1GNFkwaG9hRlVyUlVKaWMxbFZhemhLVlZSWE9WWnBkek5sUmtkQmFYSkJkazlhUVdSM1RGaE9PWHBqV0VSbE9IcFhaVzFUVmk5Rk1YZHFhV05aZDNaMWQybFpWbUo1VTAwNVdHSldjelV2Y1RobVRqaGxhSGxuTTBKbFQyRk5lVEpWWjNOT1JrNVVZaTlxWlRaT1VuRjJjR0ZXUjBJMlVYaHhjVVl6ZGxsVFYzVnlSVE4xZEVrdmIwTmpUa3hzZEU1b1IyWlJlR0Z5ZDNkb1NFcHRkVmhCUjBJNFZFeGplVTFxWm1KR2IySkdhbVYyYUZKcmIzcEdXak5RVkdGMVJTdElhM0ZCWkRoUFZUSjVSbVl2YzFocldVbE1UMFpCYlVVd0wwWlVSR2gxZVZGR09FNTNRV2hEVjBSc1RrUnJRM2R6TmtGMVJUTlBZMDV0TDBkUFpHTlFWa2hNTTFCTFRHOTJWMHhLSzNaMWMyaE1jazVhU25nMWNXRjROMmRpY0U1NFZXaGhSM05TYmpGRVZESlJkRk5XWlM4MFEzWTFPWGQyTDNGblZEUlpVbEJWT1dkVU5rOU5RWFpFV1dOcWNYZE5XbWxISzA5blZqQjJlRE5LUldaMk1IZFBVbWRpVkRKaU1VNXVUM1JLTW14VVRsQkVPWGxvVmk4NVJqazJNV2xaVVVNd1UxazkuM25zbXZUTGFncXB0QTNYamRiZWtxNkVHcWY0RUttWHRjenYwdGRLUGVlaEV0cHZqVm5ZUDc3X2tzR1lNQWxGbXMwdzQ4X0Joc0VHeUF6MDV5R1FnUUE%3D",
                "_eventId": "submit", "submit": ""}
        headers = {"Accept": "application/json, text/plain, */*", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                   "Content-Type": "application/json", "Origin": "http://ops.test.ximalaya.com", "Referer": url,
                   "Upgrade-Insecure-Requests": "1"}
        r = s.post(url, data=json.dumps(body), headers=headers)
        cookieValue = "JSESSIONID="+s.cookies.get_dict()["JSESSIONID"] + "; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN"
        # for arr in array:
        #     if arr.find('JSESSIONID') >= 0 or arr.find('bl0gm1HBTB') >= 0:
        #         cookieValue += arr + ';'
        return cookieValue
    # 读取data.yaml文件中的数据
    @classmethod
    def get_data(cls):
        yaml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.yaml")
        print(yaml_path)
        try:
            # 打开文件
            with open(yaml_path, "r", encoding="utf-8") as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                print(type(data))
                return data
        except Exception as e:
            return  e
            # return None
if __name__ == '__main__':
    print(Common.get_data())