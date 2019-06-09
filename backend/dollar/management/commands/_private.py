from dollar.models import DollarClp
from datetime import datetime, timedelta
import pytz


def check_last_dollar(data_dolar):
    """TO DO"""
    yesterday = datetime.strptime(data_dolar[0]["fecha"], '%Y-%m-%dT%H:%M:%S.%fZ') - timedelta(days=1)
    return yesterday


def insert_dollar(list_data: list):
    """Insert the elements in BD"""
    for data_dolar in list_data:
        print(data_dolar)
        if len(data_dolar) == 1:
            yesterday = datetime.strptime(data_dolar[0]["fecha"], '%Y-%m-%dT%H:%M:%S.%fZ') - timedelta(days=1)
            last_dollar = DollarClp.objects.filter(date=yesterday)  # yesterday filter
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
            new_dollar.date_update = datetime.now(pytz.timezone('Chile/Continental'))
            new_dollar.business_day = True
            new_dollar.save()
        elif len(data_dolar) == 0:
            print("resgistro viene vacio")
            last_dollar = DollarClp.objects.all().order_by('date')
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
            new_dollar.date_update = datetime.now(pytz.timezone('Chile/Continental'))
            new_dollar.business_day = False
            new_dollar.save()
        else:
            raise Exception("Cantidad de elementos no esperada")