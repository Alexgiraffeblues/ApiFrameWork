import json
from config import BASE_DIR

class ReadUtil:
    def get_data(path):
        with open(BASE_DIR + path, encoding = 'utf-8') as f:
            data = json.load(f)
            
        new_data_list = []
        
        for i in data:
            i.pop('desc')
            new_data_list.append(tuple(i.values()))
            
        return new_data_list