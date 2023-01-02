import os
from unittest import result
import requests
import csv
import datetime
import pandas as pd
import time
import smtplib

  
#from datetime import date, timedelta
import time
print("\n\n\n\n")
print("you're about to see the status of your webservices")
#get current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#get cureent date
CurrentDate=datetime.date.today()  
days = datetime.timedelta(0)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y-%m-%d')
#%d is for date  
#%m is for month  
#Y is for Year  
print(final_date) 

#os.remove("status.csv")

#result1=[]
#calling the webservices dictionary to confirm the status
BASE_URL = {
    #'service1':'https://fakestoreapi.com',
    #'service2':'https://fakestoreapi.com/1',
    #'service3':'https://api.github.com/users/defunkt',
    'sevice4':'https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&hourly=temperature_2m'
}
#calling the webservices dictionary to confirm the status
for key, value in BASE_URL.items():
        response = requests.get(f"{value}")
        #response1 = requests.get('https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&hourly=temperature_2m', timeout=5)
        result = response.json()
        #result2 = response.status_code
        #result=f'Status of {value} ({key})  is {result2} as at {final_date} {current_time}'
        #result1.append(result)
        
        #print(result.split('\n'))
        #print(result)
        new = pd.DataFrame.from_dict(result)
        #print(new)
        
        new1=new[new.columns.difference(['latitude','logitude','elevation',  'generationtime_ms', 'hourly_units', 'longitude ', 'timezone', 'timezone_abbreviation', 'utc_offset_seconds','longitude','timezone'])]
        #print(new1)
        #data=new.loc[:,'hourly']
       # me=data.to_dict
        #print(data)
        #new3 = pd.DataFrame.from_dict(data)
        #new3 = pd.DataFrame.from_dict(me)
        #
        # print(new3)

        #new2=new1[['hourly']]
        #new2 = pd.DataFrame.from_dict(new1)
        #print(data)
        #new3.to_csv('file_name.csv')
        #data=new2
        #new4 = pd.DataFrame.from_dict(data)
        #print(new4)
        for key, val in new1.items():
            #for i in val:
            #print(val[0])
            #print(val[1])
            list_item={'TIME':val[0],'TEMPERATURE_2M':val[1]}
            df = pd.DataFrame(list_item) 
            print(df)
            df.to_csv('so.csv', index=False)
#df = pd.read_csv('so.csv')
# print(df)
       
                            
                             