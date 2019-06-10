from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta

from dollar.models import DollarClp
from dollar.management.commands._private import make_date_range, make_urls, make_response, insert_dollar


class Command(BaseCommand):
    help = 'populate the dollar values'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('populate', nargs='+', type=str)

    def handle(self, *args, **options):
        if options["populate"]:
            if "all" in options["populate"]:
                date_today = datetime.today().strftime("%Y%m%d")
                list_dates = make_date_range("20180101", date_today)
                urls_data = make_urls(list_dates)
                list_response = make_response(urls_data)
                insert_dollar(list_response)
            elif "daily" in options["populate"]:
                date_today = datetime.today().strftime("%Y%m%d")
                list_dates = make_date_range(date_today, date_today)
                urls_data = make_urls(list_dates)
                list_response = make_response(urls_data)
                insert_dollar(list_response)
            else:
                list_dates = make_date_range("20180101", options["populate"][0])
                urls_data = make_urls(list_dates)
                list_response = make_response(urls_data)
                insert_dollar(list_response)


