import requests, sys
sys.path.insert(0, r'C:\Users\长颈鹿蓝调\Desktop\学习\黑马_软件测试\代码\Python学习代码\2022.8.24')
from ApiFrameWork.api.Tpshop_register_api import TPshopRegisterApi
from ApiFrameWork.common.assert_util import AssertUtil
from ApiFrameWork.common.read_util import ReadUtil
from parameterized import parameterized

class TestTPshopRegister:
    
    # 创建session对象， 发送验证码请求
    def setup(self):
        self.session = requests.session()
        TPshopRegisterApi.get_register_code_api(self.session)
    
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/TPshop_register_data.json'))
    def test_register(self, body, expect):
        response = TPshopRegisterApi.register_api(self.session, body)
        AssertUtil.assert_01(response, expect)