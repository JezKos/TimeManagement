from report_queries import Queries
from datetime import datetime, timedelta

query = Queries()
today = datetime.today()
today_date = today.strftime('%Y-%m-%d')
start_date = today - timedelta(days = 7)
start_date = start_date.strftime('%Y-%m-%d')
#print(today_date, start_date)


df_weekly = query.get_daily_report(start_date, today_date)

df_daily = query.get_daily_report(today_date, today_date)

#print(df_daily)

query.close_connections()

try:
	df_weekly.to_csv('weeklyreport.csv', index = False, mode='w')
except Exception as e:
	print(e)

try:
	df_daily.to_csv('dailyreport.csv', index = False, mode='w')
except Exception as e:
	print(e)
