from populate_module import make_date_range, make_urls, make_response, insert_dollar
from datetime import datetime, timedelta

date_today = datetime.today().strftime("%Y%m%d")
# print(date_today)

list_dates = make_date_range(date_today, date_today)
urls_data = make_urls(list_dates)
list_response = make_response(urls_data)
insert_dollar(list_response)