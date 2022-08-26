import requests

class IHRMDeptManageApi:
    
    @classmethod
    def add_dept_api(cls, token, body):
        url = 'http://ihrm2-test.itheima.net/api/company/department'
        headers = {"Content-Type" : "application/json", "Authorization" : token}
        response = requests.post(url = url,headers = headers,json = body)
        return response
         
    @classmethod
    def del_dept_api(cls, token, dept_id):
        url = 'http://ihrm2-test.itheima.net/api/company/department/' + dept_id
        headers = {"Authorization" : token}
        response = requests.delete(url = url,headers = headers)
        return response
    
    @classmethod
    def set_dept_api(cls, token, dept_id, body):
        url = 'http://ihrm2-test.itheima.net/api/company/department/' + dept_id
        headers = {"Content-Type" : "application/json", "Authorization" : token}
        response = requests.put(url = url,headers = headers,json = body)
        return response
    
    @classmethod
    def search_dept_api(cls, token, dept_id):
        url = 'http://ihrm2-test.itheima.net/api/company/department/' + dept_id
        headers = {"Authorization" : token}
        response = requests.get(url = url,headers = headers)
        return response