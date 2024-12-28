import pandas as pd
import datetime
import os
from datetime import datetime, timedelta
import arrow
from scipy.stats import percentileofscore



def data_snapshot_date():
	new_path='D:\\Raid Array\\Array 2\\3. OpenHFT\\MarketData\\DailyData'
	nifty_master = pd.read_csv('D:\\Raid Array\\Array 2\\3. OpenHFT\\Project\\NiftyMaster\\Nifty_Master.csv')
	ScripCode = nifty_master['ScripCode'].values.tolist()
	ScripName = nifty_master['Name'].values.tolist()
	new_path='D:\\Raid Array\\Array 2\\3. OpenHFT\\MarketData\\DailyData'
	new_path=new_path+'\\'+str(ScripCode[0])+'.csv'
	market_data = pd.read_csv(new_path)
	timestamp_string=market_data['Datetime'].max()
	format_string = "%Y-%m-%dT%H:%M:%S"
	datetime_object = datetime.strptime(timestamp_string, format_string)
	date_obj = datetime_object.date()
	return(date_obj)