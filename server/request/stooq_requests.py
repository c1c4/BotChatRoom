import csv

import requests

from server import NotFound, ApiBaseException
from server.configuration.config import STOOQ_API


def get_to_stooq(stooq_code: str):
    url = STOOQ_API.replace('stock_code', stooq_code)
    response = requests.get(url=url)
    if response.status_code == 200:
        wrapper = csv.reader(response.text.strip().split('\n'))
        return wrapper
    elif response.status_code == 404:
        raise NotFound
    else:
        raise ApiBaseException
