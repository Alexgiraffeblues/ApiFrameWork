import sys
sys.path.insert(0, r'C:\Users\长颈鹿蓝调\Desktop\学习\黑马_软件测试\代码\Python学习代码\2022.8.24')
from ApiFrameWork.api.IHRM_emp_manage_api import IHRMEmpManageApi
from ApiFrameWork.common.token_util import TokenUtil
from ApiFrameWork.common.assert_util import AssertUtil
from ApiFrameWork.common.read_util import ReadUtil
from parameterized import parameterized

class TestIHRMEmpManage:
    id = ''
    
    def setup_class(self):
        self.token = TokenUtil.get_IHRM_token()
    
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_add_emp_data.json'))
    def test_add_emp(self, body, expect):
        response = IHRMEmpManageApi.add_emp_api(self.token, body)
        TestIHRMEmpManage.id = response.json().get('data')['id']
        AssertUtil.assert_02(response, expect)
    
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_set_emp_data.json'))
    def test_set_emp(self, body, expect):
        response = IHRMEmpManageApi.set_emp_api(self.token, TestIHRMEmpManage.id, body)
        AssertUtil.assert_02(response, expect)
    
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_search_emp_data.json'))
    def test_search_emp(self, expect):
        response = IHRMEmpManageApi.search_emp_api(self.token, TestIHRMEmpManage.id)
        AssertUtil.assert_02(response, expect)
    
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_del_emp_data.json'))
    def test_del_emp(self, expect):
        response = IHRMEmpManageApi.del_emp_api(self.token, TestIHRMEmpManage.id)
        AssertUtil.assert_02(response, expect)