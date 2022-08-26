class TPshopLoginApi:
    
    # 封装验证码的接口
    @classmethod
    def get_verify_code_api(cls, session):
        # 发送验证码请求
        verify_code_url = 'http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify'
        session.get(verify_code_url)
    
    # 封装登录的接口
    @classmethod
    def login_api(cls, session, login_body):
        login_url = 'http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login'
        login_headers = {"Content-Type":"application/x-www-form-urlencoded"}
        login_response = session.post(url = login_url, headers = login_headers, data = login_body)
        return login_response