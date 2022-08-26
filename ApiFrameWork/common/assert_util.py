class AssertUtil:
          
    # 断言方式01
    @classmethod
    def assert_01(cls, response, expect):
        assert expect['status_code'] == response.status_code
        assert expect['status'] == response.json().get('status')
        assert expect['msg'] == response.json().get('msg')
        
    # 断言方式02
    @classmethod
    def assert_02(cls, response, expect):
        assert expect['status_code'] == response.status_code
        assert expect['success'] == response.json().get('success')
        assert expect['code'] == response.json().get('code')
        assert expect['message'] == response.json().get('message')