import sys
sys.path.insert(0, r'C:\Users\长颈鹿蓝调\Desktop\学习\黑马_软件测试\代码\Python学习代码\2022.8.24')
from ApiFrameWork.common.token_util import TokenUtil
from ApiFrameWork.api.IHRM_dept_manage_api import IHRMDeptManageApi
from ApiFrameWork.common.read_util import ReadUtil
from ApiFrameWork.common.assert_util import AssertUtil
from parameterized import parameterized

class TestIHRMDeptManage:
    id = ''
    
    def setup_class(self):
        self.token = TokenUtil.get_IHRM_token()
    
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_add_dept_data.json'))
    def test_add_dept(self, body, expect):
        response = IHRMDeptManageApi.add_dept_api(self.token, body)
        TestIHRMDeptManage.id = response.json().get('data')['id']
        AssertUtil.assert_02(response, expect)
        
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_search_dept_data.json'))
    def test_search_dept(self, expect):
        response = IHRMDeptManageApi.search_dept_api(self.token, TestIHRMDeptManage.id)
        print(response.json())
        AssertUtil.assert_02(response, expect)
        
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_set_dept_data.json'))
    def test_set_dept(self, body, expect):
        response = IHRMDeptManageApi.set_dept_api(self.token, TestIHRMDeptManage.id, body)
        AssertUtil.assert_02(response, expect)
        
    @parameterized.expand(ReadUtil.get_data('/ApiFrameWork/data/IHRM_del_dept_data.json'))
    def test_del_dept(self, expect):
        response = IHRMDeptManageApi.del_dept_api(self.token, TestIHRMDeptManage.id)
        AssertUtil.assert_02(response, expect)