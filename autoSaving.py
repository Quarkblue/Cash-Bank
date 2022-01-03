import json
import os

class AutoSave():
    
    def __init__(self):
        self.file_path = 'data\\dhan-rashi.json'
        self.fSize = os.path.getsize(self.file_path)
        
    
    
    def get_dateDiff(self, user):
        with open(self.file_path, 'r+') as jsFileObj:
            data = json.load(jsFileObj)
            start_date_str = data[user]["basics"]["date-registered"]
            start_date_lst = start_date_str.split("-")
            start_date = date(int(start_date_lst[0]),int(start_date_lst[1]),int(start_date_lst[2]))