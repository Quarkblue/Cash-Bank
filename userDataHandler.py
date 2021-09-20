import json
import os
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

class UserDataHandler():
    
    def __init__(self) -> None:
        self.file_path_users = 'data\\users.json'
        self.file_path_data = 'data\data'
        self.fSize = os.path.getsize(self.file_path_users)


    def checkIfUserExists(self, username):
        with open(self.file_path_users, 'r') as jsfile:
            data = json.load(jsfile)
            
            if username in list(data.keys()):
                return True
            else:
                return False
            
            
    def login(self, username, password):
        with open(self.file_path_users, 'r') as jsfile:
            data = json.load(jsfile)
            password_hash = data[username]["password"]
            
            match = check_password_hash(password_hash, password)
            
            return match
        
        
    def signup(self, username, password):
        with open(self.file_path_users, 'r+') as jsfile:
            data = json.load(jsfile)
            data[username] = {"password": generate_password_hash(password)}
            jsfile.seek(0,0)
            json.dump(data,jsfile)
            
            
    def signup_need(self):
        if self.fSize == 0 or self.fSize == 2:
            return True
        else:
            False
            
            
        




