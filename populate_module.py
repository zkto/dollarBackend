from datetime import datetime, timedelta

import requests
import json
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'dollarMonitor.settings'
django.setup()

from dollar.models import DollarClp

BASE_URL_INDICADOR = "https://mindicador.cl/api/dolar/"


def make_date_range(init_date: str, end_date: str) -> list:
    """Genera una lista de fechas en el formato dd-mm-YYYY
    con input de fechas YYYYmmdd"""
    obj_init = datetime.strptime(init_date, "%Y%m%d")
    obj_end = datetime.strptime(end_date, "%Y%m%d")
    days_difference = (obj_end - obj_init).days + 1  # inclusive el ultimo dia
    list_of_dates = list()
    for i in range(days_difference):
        date_new = obj_init + timedelta(days=i)
        list_of_dates.append(date_new.strftime("%d-%m-%Y"))
    return list_of_dates


def make_urls(list_dates: list) -> list:
    """Genera las url de consulta de dolar por fecha"""
    new_list = list()
    for date_value in list_dates:
        new_list.append(BASE_URL_INDICADOR + date_value)
    return new_list


def parse_dollar_request(content_request: str) -> list:
    """Formatea en contenido del request"""
    content_json = json.loads(content_request)
    if content_json["unidad_medida"] == "Pesos" and content_json["codigo"] == "dolar":
        return content_json["serie"]


def make_response(list_urls: list) -> list:
    """Consulta get de las url"""
    list_response = list()
    for url in list_urls:
        response = requests.get(url)
        list_response.append(parse_dollar_request(response.content))
    return list_response


def insert_dollar(list_data: list):
    """Inserta elementos en BD"""
    for data_dolar in list_data:
        print(data_dolar)
        if len(data_dolar) == 1:
            yesterday = datetime.strptime(data_dolar[0]["fecha"], '%Y-%m-%dT%H:%M:%S.%fZ') - timedelta(days=1)
            last_dollar = DollarClp.objects.filter(date=yesterday)  # filtrar ayer
            if len(last_dollar) >= 1:
                last_dollar = last_dollar.last()
                print("registro anterior fecha {0}, valor {1}".format(last_dollar.date, last_dollar.price))
                diff = data_dolar[0]["valor"] - last_dollar.price
            else:
                diff = 0
            new_dollar = DollarClp()
            new_dollar.price = data_dolar[0]["valor"]
            new_dollar.price_difference = diff
            new_dollar.date = datetime.strptime(data_dolar[0]["fecha"], '%Y-%m-%dT%H:%M:%S.%fZ')
            new_dollar.date_update = datetime.today()
            new_dollar.week_value = True
            new_dollar.save()
        elif len(data_dolar) == 0:
            print("resgistro viene vacio")
            last_dollar = DollarClp.objects.all().order_by('date')
            print(type(last_dollar))
            print("cantidad registros", len(last_dollar))
            if len(last_dollar) >= 1:
                last_dollar = last_dollar.last()
                yest_price = last_dollar.price
                yest_date = last_dollar.date
            else:
                print("no existe data suficiente para registrar datos")
                continue
            print("fecha anterior", yest_date)
            print("fecha actual", yest_date + timedelta(days=1))
            new_dollar = DollarClp()
            new_dollar.price = yest_price
            new_dollar.price_difference = 0
            new_dollar.date = yest_date + timedelta(days=1)
            new_dollar.date_update = datetime.today()
            new_dollar.week_value = False
            new_dollar.save()
        else:
            raise Exception("Cantidad de elementos no esperada")
