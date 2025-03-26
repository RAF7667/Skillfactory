import requests
import json
from config import keys
from config import API_KEY



class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{quote_ticker}/{base_ticker}/{amount}'

        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()

            if data['result'] != 'success':
                raise APIException(f"Ошибка API: {data.get('error-type', 'Unknown')}")

            return data['conversion_result']

        except requests.exceptions.RequestException as e:
            raise APIException(f"Ошибка соединения: {str(e)}")
