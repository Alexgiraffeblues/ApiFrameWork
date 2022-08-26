import sys
sys.path.insert(0, r'C:\Users\长颈鹿蓝调\Desktop\学习\黑马_软件测试\代码\Python学习代码\2022.8.24')
from parameterized import parameterized
from ApiFrameWork.api.IHRM_login_api import IHRMLoginApi
from ApiFrameWork.common.assert_util import AssertUtil
from ApiFrameWork.common.read_util import ReadUtil

class TestIHRMLogin:
    
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_login_data.json'))
    def test_login(self, body, expect):
        response = IHRMLoginApi.login_api(body)
        AssertUtil.assert_02(response, expect)