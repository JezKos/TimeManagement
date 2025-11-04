from report_queries import Queries



query = Queries()

df = query.get_daily_report('2025-11-02',  '2025-11-06')
print(df)

query.close_connections()
