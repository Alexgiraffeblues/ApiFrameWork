class TPshopRegisterApi:
    
    # 封装验证码的接口
    @classmethod
    def get_register_code_api(cls, session):
        verify_code_url = 'http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&type=user_reg&r=0.6710677555863709'
        session.get(verify_code_url)
        
    # 封装注册的接口
    @classmethod
    def register_api(cls, session, register_body):
        register_url = 'http://hmshop-test.itheima.net/Home/User/reg.html'
        register_headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
        register_response = session.post(url = register_url, headers = register_headers, data = register_body)
        return register_response