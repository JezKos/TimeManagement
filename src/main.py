from report_queries import Queries
from datetime import datetime, timedelta

query = Queries()
today = datetime.today()
today_date = today.strftime('%Y-%m-%d')
start_date = today - timedelta(days = 7)
start_date = start_date.strftime('%Y-%m-%d')
print(today_date, start_date)


df = query.get_daily_report(start_date, today_date)
print(df)

query.close_connections()
df.to_csv('dailyreport.csv', index = False)
