from datetime import datetime, timedelta

import requests
import json
import os
import django


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

