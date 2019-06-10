from dollar.models import DollarClp
from datetime import datetime, timedelta
import pytz
import requests
import json


BASE_URL_INDICADOR = "https://mindicador.cl/api/dolar/"


def make_date_range(init_date: str, end_date: str) -> list:
    """Generates a list of dates in the format dd-mm-YYYY
    with input of dates YYYYmmdd"""
    obj_init = datetime.strptime(init_date, "%Y%m%d")
    obj_end = datetime.strptime(end_date, "%Y%m%d")
    days_difference = (obj_end - obj_init).days + 1  # inclusive el ultimo dia
    list_of_dates = list()
    for i in range(days_difference):
        date_new = obj_init + timedelta(days=i)
        list_of_dates.append(date_new.strftime("%d-%m-%Y"))
    return list_of_dates


def make_urls(list_dates: list) -> list:
    """Generate dollar query url by date"""
    new_list = list()
    for date_value in list_dates:
        new_list.append(BASE_URL_INDICADOR + date_value)
    return new_list


def parse_dollar_request(content_request: str) -> list:
    """format the content of the request"""
    content_json = json.loads(content_request)
    if content_json["unidad_medida"] == "Pesos" and content_json["codigo"] == "dolar":
        return content_json["serie"]


def make_response(list_urls: list) -> list:
    """make a list of results based on url responses"""
    list_response = list()
    for url in list_urls:
        response = requests.get(url)
        list_response.append(parse_dollar_request(response.content))
    return list_response


def insert_dollar(list_data: list):
    """Insert the elements in BD"""
    for data_dolar in list_data:
        if len(data_dolar) == 1:
            yesterday = datetime.strptime(data_dolar[0]["fecha"], '%Y-%m-%dT%H:%M:%S.%fZ') - timedelta(days=1)
            last_dollar = DollarClp.objects.filter(date=yesterday)  # yesterday filter
            if len(last_dollar) >= 1:
                last_dollar = last_dollar.last()
                diff = data_dolar[0]["valor"] - last_dollar.price
            else:
                diff = 0
            new_dollar = DollarClp()
            new_dollar.price = data_dolar[0]["valor"]
            new_dollar.price_difference = diff
            new_dollar.date = datetime.strptime(data_dolar[0]["fecha"], '%Y-%m-%dT%H:%M:%S.%fZ')
            new_dollar.date_update = datetime.now(pytz.timezone('Chile/Continental'))
            new_dollar.business_day = True
            new_dollar.save()
        elif len(data_dolar) == 0:
            last_dollar = DollarClp.objects.all().order_by('date')
            if len(last_dollar) >= 1:
                last_dollar = last_dollar.last()
                yest_price = last_dollar.price
                yest_date = last_dollar.date
            else:
                continue  # in this case there is not enough data to store a record
            new_dollar = DollarClp()
            new_dollar.price = yest_price
            new_dollar.price_difference = 0
            new_dollar.date = yest_date + timedelta(days=1)
            new_dollar.date_update = datetime.now(pytz.timezone('Chile/Continental'))
            new_dollar.business_day = False
            new_dollar.save()
        else:
            raise Exception("Cantidad de elementos no esperada")