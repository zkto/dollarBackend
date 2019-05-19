from datetime import datetime, timedelta

import requests

BASE_URL_INDICADOR = "https://mindicador.cl/api/dolar/"


def make_date_range(init_date, end_date):
    obj_init = datetime.strptime(init_date, "%Y%m%d")
    obj_end = datetime.strptime(end_date, "%Y%m%d")
    days_difference = (obj_end - obj_init).days
    list_of_dates = list()
    for i in range(days_difference):
        date_new = obj_init + timedelta(days=i)
        list_of_dates.append(date_new.strftime("%d-%m-%Y"))
    return list_of_dates


def make_urls(list_dates):
    new_list = list()
    for date_value in list_dates:
        new_list.append(BASE_URL_INDICADOR + date_value)
    return new_list


def make_response(list_urls):
    for url in list_urls:
        response = requests.get(url)
        print(response.content)


list_dates = make_date_range("20180101", "20190101")
urls_data = make_urls(list_dates)
make_response(urls_data)
