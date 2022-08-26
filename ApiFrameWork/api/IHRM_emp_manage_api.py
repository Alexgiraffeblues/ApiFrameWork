import requests

class IHRMEmpManageApi:
    
    @classmethod
    def add_emp_api(cls, token, body):
        url = 'http://ihrm2-test.itheima.net/api/sys/user'
        headers = {"Content-Type" : "application/json", "Authorization" : token}
        response = requests.post(url = url, headers = headers, json = body)
        return response
    
    @classmethod
    def del_emp_api(cls, token, emp_id):
        url = 'http://ihrm2-test.itheima.net/api/sys/user/' + emp_id
        headers = {"Authorization" : token}
        response = requests.delete(url = url, headers = headers)
        return response
    
    @classmethod
    def set_emp_api(cls, token, emp_id, body):
        url = 'http://ihrm2-test.itheima.net/api/sys/user/' + emp_id
        headers = {"Content-Type" : "application/json", "Authorization" : token}
        response = requests.put(url = url, headers = headers, json = body)
        return response
    
    @classmethod
    def search_emp_api(cls, token, emp_id):
        url = 'http://ihrm2-test.itheima.net/api/sys/user/' + emp_id
        headers = {"Authorization" : token}
        response = requests.get(url = url, headers = headers)
        return response