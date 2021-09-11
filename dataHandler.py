import json
import os
from datetime import date

class DataHandler():
    
    def __init__(self) -> None:
        
        self.file_path = 'data\\dhan-rashi.json'
        self.fSize = os.path.getsize(self.file_path)
        
    def getTheData(self):
        
        first_time = False
    
        with open(self.file_path, 'r+') as jsFile:
            
            if self.fSize == 0 or self.fSize == 2:
                
                first_time = True
                
            if first_time == True:
                
                total = 0
                monthly_savings = 0
                daily_savings = 0
                while True:
            
                    total = int(input("Enter total money you have/had in the starting:> "))
                
                    w_save = input("Do you want to save monthly?[Y/N] :> ")
                    
                    if w_save.lower() == 'y':
                        
                        monthly_savings = int(input("Enter how much do you want to save monthly[0 for none]:> "))

                    elif w_save.lower() == 'n':

                        daily_savings = int(input("Enter how much you want so save daily[0 for none]:> "))
                        
                    jsInput_data = {"basics":{
                                            "total": total,
                                            "monthly_savings": monthly_savings,
                                            "daily_savings": daily_savings
                                            }
                                    }
                        
                    json.dump(jsInput_data, jsFile)
                    jsFile.close()
                    break
                        
            with open(self.file_path, 'r') as jsFile:
                
                data = json.load(jsFile)
                    
                key = list(data.keys())[-1]
                
                total = data['basics']['total']
                monthly_savings = data['basics']['monthly_savings']
                daily_savings = data['basics']['daily_savings']
        
                add_savings = 0
                withd_savings = 0
                
                total_left = int(input("Enter how much money you have right now:> "))
                
                sOrw = input("Do you want to ADD[A] to savings or WITHDRAW[W]:> ")
                                
                if sOrw.lower() == 'a':

                    add_savings = int(input("Enter how much money to your savings:> "))
                    
                if sOrw.lower() == 'w':
                        
                    if key == 'basics' or data[key]['savings_total'] == 0:
                
                        print('You cannot withdraw...')
                        print('because you dont have (lol?)')
                        
                    else:
                    
                        withd_savings = int(input("Enter how much you want to remove from your savings:> "))
                        
                        if withd_savings > data[key]['total_savings']:
                            
                            withd_savings = 0
                            print("How can you withdraw more than you have?")
                            
        today = date.today()
        
        return {'today': today, 'total': total, 'total_left': total_left, 'add_savings': add_savings, 'withd_savings': withd_savings}