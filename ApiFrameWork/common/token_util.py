import sys
sys.path.insert(0, r'C:\Users\长颈鹿蓝调\Desktop\学习\黑马_软件测试\代码\Python学习代码\2022.8.24')
from ApiFrameWork.api.IHRM_login_api import IHRMLoginApi


class TokenUtil:
    @classmethod
    def get_IHRM_token(cls):
        body = {"mobile" : "13800000002","password" : "123456"}
        response =  IHRMLoginApi.login_api(body)
        token = response.json().get('data')
        return token