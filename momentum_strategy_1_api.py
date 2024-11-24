import pandas as pd
import datetime
import os
from datetime import datetime, timedelta
import arrow
from scipy.stats import percentileofscore


def momentum_strategy_1(date_delim):

		nifty_master = pd.read_csv('Nifty_Master.csv')
		ScripCode = nifty_master['ScripCode'].values.tolist()
		ScripName = nifty_master['Name'].values.tolist()


		new_path='MarketData/DailyData'
		new_path=new_path+'/'+str(ScripCode[0])+'.csv'
		market_data = pd.read_csv(new_path)
		#print(market_data)

		for code in ScripCode:
			new_path='MarketData/DailyData'
			new_path=new_path+'/'+str(code)+'.csv'
			additional_market_data=pd.read_csv(new_path)
			#market_data=market_data.append(additional_market_data)
			market_data=pd.concat([market_data, additional_market_data])
			#print(new_path)
			#print("\n")
			

		timestamp_string=market_data['Datetime'].max()
		format_string = "%Y-%m-%dT%H:%M:%S"
		datetime_object = datetime.strptime(timestamp_string, format_string)
		date_obj = datetime_object.date()
		#print(timestamp_string)
		#print(datetime_object)
		#print(date_obj)


		current_date=date_obj
		current_date=str(current_date)
		
		available_datetime=market_data['Datetime'].values.tolist()
		available_dates_pre_check=[]
		for day in available_datetime:
			converted_date=datetime.strptime(str(day), format_string).date()
			#print(converted_date)
			available_dates_pre_check.append(converted_date)

		date_match_flag_pre=0

		for date in available_dates_pre_check:
			if str(date)==date_delim:
				date_match_flag_pre=1
			

		if(date_match_flag_pre==0):
			print("Incorrect Date passed to Strategy")
			return "Error 401 - Date Passed is not a Trading Day"

		current_date=str(date_delim)

		#print("Printing Current Date ***************")
		#print(current_date)
		date_format = 'YYYY-MM-DD'

		r1y_date = arrow.get(current_date, date_format).shift(years=-1)
		r1y_date = r1y_date.format(date_format)
		#print(r1y_date)

		r6m_date = arrow.get(current_date, date_format).shift(months=-6)
		r6m_date = r6m_date.format(date_format)
		#print(r6m_date)

		r3m_date = arrow.get(current_date, date_format).shift(months=-3)
		r3m_date = r3m_date.format(date_format)
		#print(r3m_date)

		r1m_date = arrow.get(current_date, date_format).shift(months=-1)
		r1m_date = r1m_date.format(date_format)
		#print(r1m_date)



		available_datetime=market_data['Datetime'].values.tolist()
		available_dates=[]
		for day in available_datetime:
			converted_date=datetime.strptime(str(day), format_string).date()
			#print(converted_date)
			available_dates.append(converted_date)


		alternate_format="%Y-%m-%d"
		current_date_dtobj=datetime.strptime(current_date, alternate_format).date()
		r1y_date_dtobj=datetime.strptime(r1y_date, alternate_format).date()
		r6m_date_dtobj=datetime.strptime(r6m_date, alternate_format).date()
		r3m_date_dtobj=datetime.strptime(r3m_date, alternate_format).date()
		r1m_date_dtobj=datetime.strptime(r1m_date, alternate_format).date()

		#print(current_date_dtobj)
		#print(r1y_date_dtobj)
		#print(r6m_date_dtobj)
		#print("R3M AND R1M DATES HERE \n")
		#print(r3m_date_dtobj)
		#print(r1m_date_dtobj)
		#print(available_dates[0])

		#r1y_date_dtobj = r1y_date_dtobj - timedelta(days=1)
		#print(r1y_date_dtobj)


		#print("Date Shifting starts here -----")

		#----------------------------------------------------
		# Date Shift to ensure date is not holiday or Weekend
		# Area - R1Y Date
		#-----------------------------------------------------
		date_match_flag=0

		while date_match_flag==0:
			for date in available_dates:
				if date==r1y_date_dtobj:
					date_match_flag=1
			if date_match_flag==0:
				r1y_date_dtobj = r1y_date_dtobj - timedelta(days=1)


		#print(r1y_date_dtobj)

		#----------------------------------------------------
		# Date Shift to ensure date is not holiday or Weekend
		# Area - R6M Date
		#-----------------------------------------------------
		date_match_flag=0

		while date_match_flag==0:
			for date in available_dates:
				if date==r6m_date_dtobj:
					date_match_flag=1
			if date_match_flag==0:
				r6m_date_dtobj = r6m_date_dtobj - timedelta(days=1)


		#print(r6m_date_dtobj)



		#----------------------------------------------------
		# Date Shift to ensure date is not holiday or Weekend
		# Area - R3M Date
		#-----------------------------------------------------
		date_match_flag=0

		while date_match_flag==0:
			for date in available_dates:
				if date==r3m_date_dtobj:
					date_match_flag=1
			if date_match_flag==0:
				r3m_date_dtobj = r3m_date_dtobj - timedelta(days=1)


		#print(r3m_date_dtobj)

		#----------------------------------------------------
		# Date Shift to ensure date is not holiday or Weekend
		# Area - R1M Date
		#-----------------------------------------------------
		date_match_flag=0

		while date_match_flag==0:
			for date in available_dates:
				if date==r1m_date_dtobj:
					date_match_flag=1
			if date_match_flag==0:
				r1m_date_dtobj = r1m_date_dtobj - timedelta(days=1)


		#print(r1m_date_dtobj)





		market_data_sanitized=market_data[['Datetime','Open','ScripName','ScripCode']]
		market_data_sanitized=market_data_sanitized.drop_duplicates()
		market_data_sanitized['Datetime']=pd.to_datetime(market_data_sanitized['Datetime'], format=format_string)
		#print(market_data_sanitized)


		#print("----------------------")
		#print("Filtering Starts Here")
		#print("----------------------")

		#print("Current Date is "+ str(current_date_dtobj))

		#filtered_df = df[df['Age'] > 30]
		market_data_current=market_data_sanitized[market_data_sanitized['Datetime']==str(current_date_dtobj)]
		market_data_current.columns = ['Current_Datetime', 'Current_Price', 'ScripName','ScripCode']
		#print(market_data_current)

		market_data_r1y=market_data_sanitized[market_data_sanitized['Datetime']==str(r1y_date_dtobj)]
		market_data_r1y.columns = ['R1Y_Datetime', 'R1Y_Price', 'ScripName','ScripCode']
		#print(market_data_r1y)

		market_data_r6m=market_data_sanitized[market_data_sanitized['Datetime']==str(r6m_date_dtobj)]
		market_data_r6m.columns = ['R6M_Datetime', 'R6M_Price', 'ScripName','ScripCode']
		market_data_r6m=market_data_r6m[['R6M_Datetime', 'R6M_Price', 'ScripCode']]
		#print(market_data_r6m)

		market_data_r3m=market_data_sanitized[market_data_sanitized['Datetime']==str(r3m_date_dtobj)]
		market_data_r3m.columns = ['R3M_Datetime', 'R3M_Price', 'ScripName','ScripCode']
		market_data_r3m=market_data_r3m[['R3M_Datetime', 'R3M_Price', 'ScripCode']]
		#print(market_data_r3m)

		market_data_r1m=market_data_sanitized[market_data_sanitized['Datetime']==str(r1m_date_dtobj)]
		market_data_r1m.columns = ['R1M_Datetime', 'R1M_Price', 'ScripName','ScripCode']
		market_data_r1m=market_data_r1m[['R1M_Datetime', 'R1M_Price', 'ScripCode']]
		#print(market_data_r1m)

		momentum_data = pd.merge(market_data_current, market_data_r1y, on="ScripCode", how="left")
		momentum_data=momentum_data[['ScripCode','ScripName_x','Current_Datetime','Current_Price','R1Y_Datetime','R1Y_Price']]
		momentum_data.columns=['ScripCode','ScripName','Current_Datetime','Current_Price','R1Y_Datetime','R1Y_Price']
		momentum_data = pd.merge(momentum_data, market_data_r6m, on="ScripCode", how="left")
		momentum_data = pd.merge(momentum_data, market_data_r3m, on="ScripCode", how="left")
		momentum_data = pd.merge(momentum_data, market_data_r1m, on="ScripCode", how="left")
		#print(momentum_data)


		momentum_data_master=momentum_data
		momentum_data_master['R1Y_return']=((momentum_data_master['Current_Price']-momentum_data_master['R1Y_Price'])/momentum_data_master['R1Y_Price'])
		momentum_data_master['R6M_return']=((momentum_data_master['Current_Price']-momentum_data_master['R6M_Price'])/momentum_data_master['R6M_Price'])
		momentum_data_master['R3M_return']=((momentum_data_master['Current_Price']-momentum_data_master['R3M_Price'])/momentum_data_master['R3M_Price'])
		momentum_data_master['R1M_return']=((momentum_data_master['Current_Price']-momentum_data_master['R1M_Price'])/momentum_data_master['R1M_Price'])


		#all_percentiles = [percentileofscore(dataset, value, kind='strict') for value in dataset]
		R1Y_return_list=momentum_data_master['R1Y_return'].values.tolist()
		R1Y_percentile_list = [percentileofscore(R1Y_return_list, value, kind='strict') for value in R1Y_return_list]

		R6M_return_list=momentum_data_master['R6M_return'].values.tolist()
		R6M_percentile_list = [percentileofscore(R6M_return_list, value, kind='strict') for value in R6M_return_list]

		R3M_return_list=momentum_data_master['R3M_return'].values.tolist()
		R3M_percentile_list = [percentileofscore(R3M_return_list, value, kind='strict') for value in R3M_return_list]

		R1M_return_list=momentum_data_master['R1M_return'].values.tolist()
		R1M_percentile_list = [percentileofscore(R1M_return_list, value, kind='strict') for value in R1M_return_list]



		momentum_data_master['R1Y_percentile']=R1Y_percentile_list
		momentum_data_master['R6M_percentile']=R6M_percentile_list
		momentum_data_master['R3M_percentile']=R3M_percentile_list
		momentum_data_master['R1M_percentile']=R1M_percentile_list

		momentum_data_master['Momentum_Score']=(momentum_data_master['R1Y_percentile']+momentum_data_master['R6M_percentile']+momentum_data_master['R3M_percentile']+momentum_data_master['R1M_percentile'])/4
		momentum_data_export=momentum_data_master[['ScripCode','ScripName','R1Y_return','R6M_return','R3M_return','R1M_return','R1Y_percentile','R6M_percentile','R3M_percentile','R1M_percentile','Momentum_Score']]
		momentum_data_export = momentum_data_export.sort_values(by=['Momentum_Score'], ascending=False)

		momentum_data_export_sanitized=momentum_data_export[['ScripName','R1Y_return','R6M_return','R3M_return','R1M_return','Momentum_Score']]
		momentum_data_export_sanitized['R1Y_return']=momentum_data_export_sanitized['R1Y_return']*100
		momentum_data_export_sanitized['R6M_return']=momentum_data_export_sanitized['R6M_return']*100
		momentum_data_export_sanitized['R3M_return']=momentum_data_export_sanitized['R3M_return']*100
		momentum_data_export_sanitized['R1M_return']=momentum_data_export_sanitized['R1M_return']*100
		#momentum_data_export_sanitized.columns = ['Scrip Name','R1Y Return','R6M Return','R3M return','R1M_return','Momentum Score']
		#print(momentum_data_export)
		return momentum_data_export_sanitized


		#print(momentum_data_master)
		#print(R1Y_percentile_list)
		#momentum_data_master.to_csv('momentum_data_master_all.csv')
		#momentum_data_export.to_csv('momentum_data_export.csv')