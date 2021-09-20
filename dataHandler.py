import json
import os
from datetime import date

class DataHandler():
    
    def __init__(self) -> None:
        
        self.file_path = 'data\\dhan-rashi.json'
        self.fSize = os.path.getsize(self.file_path)
        self.first_time = False
        
    
    
    def saveUserData(self, user, jsData):
        with open(self.file_path, 'r+') as jsFileObj:
            data = json.load(jsFileObj)
            last_entry_from_input = list(data.keys())[-1]
            last_entry_from_data = list(jsData.keys())[-1]
            entry_no_input = int(last_entry_from_input[6:])
            entry_no_data = 0
            
            if last_entry_from_data == 'basics':
                if entry_no_input == 1:
                    jsFileObj.seek(0,0)
                    json.dump(jsData, jsFileObj)
                    
            elif 'entry_' in last_entry_from_data:
                if entry_no_data < entry_no_input:
                    jsFileObj.seek(0,0)
                    json.dump(jsData, jsFileObj)
                    
                    
                    
    def checkIfBasicInput(self):
        with open(self.file_path, 'r+') as jsFile:
            jsData = json.load(jsFile)
            
            if self.fSize == 0 or self.fSize == 2:
                self.first_time = True
                
            if self.first_time:
                return (True,)
            
            elif not self.first_time:
                
                return (False, jsData)
            
            
    # def save_daily_input(self, data, jsData, user):
        
    #     with open(self.file_path, 'r') as jsFile:
            
    #         jsData = json.loads(jsFile.read())
    #         keys = list(jsData.keys())
    #         if jsData != {}:
    #             last_key = list(jsData[user].keys())[-1]
    #             if last_key == 'basics':
    #                 return True
                
    #             elif 'entry_' in last_key:
    #                 return False
                
        

    
        
        
        