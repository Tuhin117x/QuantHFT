import pandas as pd
import datetime
import os


from py5paisa import FivePaisaClient
cred={
    "APP_NAME":"5P59704099",
    "APP_SOURCE":"24754",
    "USER_ID":"gTdR58TPfbj",
    "PASSWORD":"QkzqzMNFvet",
    "USER_KEY":"SyKsXvXfGbrllnbrfsRWz3a6nVTcVysq",
    "ENCRYPTION_KEY":"aKqK8EYVrzGvmQuTBxuiwwWbzRuh63CM"
    }

nifty_master = pd.read_csv('Nifty_Master.csv')
#print(nifty_master)
#print(nifty_master['ScripCode'])
#print(nifty_master['Name'])

ScripCode = nifty_master['ScripCode'].values.tolist()
#print(ScripCode)
ScripName = nifty_master['Name'].values.tolist()
#print(ScripName)




client = FivePaisaClient(cred=cred)
client.get_totp_session('59704099',input("enter totp >>> "),'150395')

new_path='MarketData/DailyData'
os.chdir(new_path)

i=0
for code in ScripCode:
    #print(code)
    df=client.historical_data('N','C',code,'1d','2022-01-01',str(datetime.datetime.today()).split()[0])
    df['ScripName']=ScripName[i]
    df['ScripCode']=code
    file_name=str(code)+'.csv'
    print("Saving Data Frame for Scrip "+file_name)
    df.to_csv(file_name)
    i=i+1
    #print(df)

#df=client.historical_data('N','C',10990,'1d','2022-01-01',str(datetime.datetime.today()).split()[0])
#df['scrip_name']='Radico Khaitan'
#df.to_csv('test.csv')

#print(df)