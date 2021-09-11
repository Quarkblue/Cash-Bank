import json
import os
from datetime import date

file_path = 'data\\dhan-rashi.json'


def getTheData():
    """ 
    simply inputs the data from the user whilst checking if the data is correct
    :return data:
    """
    
    file_path = 'data\\dhan-rashi.json'
    
    fSize = os.path.getsize(file_path)
    
    first_time = False
    
    with open(file_path, 'r+') as jsFile:
        
        # Check if the user is first the data is inputed first time
        if fSize == 0 or fSize == 2:
            
            first_time = True
            # jsFile.seek(1, 0)
        
        # If data is inputed first time
        if first_time == True:
            
            total = 0
            monthly_savings = 0
            daily_savings = 0
            while True:
        
                # get the total, monthly_savings[Y/N], Daily_savings[Y/N]
                total = int(input("Enter total money you have/had in the starting:> "))
            
                w_save = input("Do you want to save monthly?[Y/N] :> ")
                
                # if monthly_savings[Y]
                if w_save.lower() == 'y':
                    
                    # get how much to save monthly...
                    monthly_savings = int(input("Enter how much do you want to save monthly[0 for none]:> "))

                # if daily_savings[Y]
                elif w_save.lower() == 'n':

                    # get how much to save daily...
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
                    
                
         
        with open(file_path, 'r') as jsFile:
            
            data = json.load(jsFile)
                
            key = list(data.keys())[-1]
            
            total = data['basics']['total']
            monthly_savings = data['basics']['monthly_savings']
            daily_savings = data['basics']['daily_savings']
    
            add_savings = 0
            withd_savings = 0
            
            # get how much money they have left right now
            total_left = int(input("Enter how much money you have right now:> "))
            
            # get do they want to add money to savings or withdraw from savings[Y/N]
            sOrw = input("Do you want to ADD[A] to savings or WITHDRAW[W]:> ")
            
            
            # if add
            if sOrw.lower() == 'a':

                # get how much money to add to savings
                add_savings = int(input("Enter how much money to your savings:> "))
                
            # if withd
            if sOrw.lower() == 'w':
                
                # check if its the first time they are inputing the data after basics
                
                # if first time or there are no savings
                if key == 'basics' or data[key]['savings_total'] == 0:
                
                    # print you cannot withdraw if you havent saved yet
                    print('You cannot withdraw...')
                    print('because you dont have (lol?)')
                    
                # else
                else:
                
                    # get how much to withdraw
                    withd_savings = int(input("Enter how much you want to remove from your savings:> "))
                    
                    if withd_savings > data[key]['total_savings']:
                        
                        withd_savings = 0
                        print("How can you withdraw more than you have?")
                        
    
    # get the date for the entry
    today = date.today()
    
    
    
    return {'today': today, 'total': total, 'total_left': total_left, 'add_savings': add_savings, 'withd_savings': withd_savings}


def evaluateTheData(data):
    """
    Evaluates and converts the data inputed by the user into json form to store in the file
    :param data:
    :return jsData:
    """
    
    with open(file_path, 'r') as jsFile:
        
        jsData = json.load(jsFile)
        
        gained = 0
        spent = 0
        
        saved_today = data['add_savings']
        withdrawed = data['withd_savings']
        
        key = list(jsData.keys())[-1]
        
        if key == 'basics':
            
            total = data['total']
            
            
            date = str(data['today'])
            
            total_left_to_spend = data['total']
            
            saving_total = data['add_savings']
            
            total_spent = 0
            
            if data['total_left'] > data['total']:
                
                gained = data['total_left'] - data['total']
                
            elif data['total'] > data['total_left']:
                
                spent = data['total'] - data['total_left']
                
                total_spent = spent
                
            
            if data['add_savings'] != 0:
                
                total_left_to_spend = data['total'] - ((spent + data['add_savings']) - gained)
                
                
            jsData['entry_1'] = {
                                "date": date,
                                "spent": spent,
                                "gained": gained,
                                "saved_today": saved_today,
                                "withdrawed": withdrawed,
                                "savings_total": saving_total,
                                "total_left_to_spend": total_left_to_spend,
                                "total": total,
                                "total_spent": total_spent
                                }
                               
            
        elif key != 'basics' and 'entry_' in key:
            
            last_entry_no = int(key[6:])
            current_entry_no = last_entry_no + 1
            
            date = str(data['today'])
            
            total_spent = jsData[key]['total_spent']
            
            total_left_to_spend = jsData[key]['total_left_to_spend']
            
            savings_total = jsData[key]['savings_total']
            
            if data['total_left'] > total_left_to_spend:

                gained = data['total_left'] - total_left_to_spend

            elif total_left_to_spend > data['total_left']:

                spent = jsData[key]['total_left_to_spend'] - data['total_left']

                total_spent += spent

            if data['add_savings'] != 0:

                total_left_to_spend -= ((spent + data['add_savings']) - gained)

            elif data['withd_savings'] != 0:

                total_left_to_spend += ((data['withd_savings'] + gained) - spent)


            savings_total = savings_total + (data['add_savings'] - data['withd_savings'])

            total = data['total']

            jsData[f'entry_{current_entry_no}'] = {
                                                "date": date,
                                                "spent": spent,
                                                "gained": gained,
                                                "saved_today": saved_today,
                                                "withdrawed": withdrawed,
                                                "savings_total": savings_total,
                                                "total_left_to_spend": total_left_to_spend,
                                                "total": total,
                                                "total_spent": total_spent
                                                }
    return jsData

def saveInFile(jsData):
    with open(file_path, 'r+') as jsFileObj:
        data = json.load(jsFileObj)
        
        
        last_entry_from_input = list(jsData.keys())[-1]
        print(jsData[last_entry_from_input])
        
        last_entry_from_data = list(data.keys())[-1]
        
        entry_no_input =  int(last_entry_from_input[6:])
        entry_no_data = 0
        
        if last_entry_from_data == 'basics':
            
            if entry_no_input == 1:
                
                jsFileObj.seek(0,0)
                json.dump(jsData, jsFileObj)
                
                return "The data was saved successfully as entry number 1"
                
            else:
                
                return "The file does not have first entry"
        
        elif 'entry_' in last_entry_from_data:
            
            if entry_no_data < entry_no_input:
                
                jsFileObj.seek(0,0)
                json.dump(jsData, jsFileObj)
                
                return f"The data was saved successfully as entry number {entry_no_input}"
            
            else:
                
                return "The cannot be entered as the entry number of the inputed data is greater than the last entry number"
            
        else:
            
            return "The file is not ready to store this data"
        


# {'today': datetime.date(2021, 6, 8), 'total': 10000, 'total_left': 9000, 'add_savings': 1000, 'withd_savings': 0}

def displayData():
    

    with open(file_path, 'r+') as jsFile:
        eData = json.load(jsFile)                                     # Existing data
        last_entry = list(eData.keys())[-1]
    
    ans = True
    while ans:
        
        today = str(date.today())
        
        if last_entry != 'basics' and 'entry_' in last_entry:
            
            last_date = eData[last_entry]['date']
            
            if last_date == today:

                print("1.Edit todays data")
                print("2.See the data already stored")
                
        



if __name__ == '__main__':
    # data = getTheData()
    # print(data)
    data = getTheData()
    jsData = evaluateTheData(data)
    output = saveInFile(jsData)
    print(output)