import requests

class IHRMLoginApi:
    
    # 封装登录的接口
    @classmethod
    def login_api(self, body):
        url = 'http://ihrm2-test.itheima.net/api/sys/login'
        headers = {"Content-Type" : "application/json"}
        response = requests.post(url = url, headers = headers, json = body)
        return response