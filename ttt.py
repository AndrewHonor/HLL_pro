from flask import Flask, request, render_template_string
import requests
app = Flask(__name__)
def get_bitcoin_value(currency):
    """
    price of one bit_ka in valute.

    Args:
        currency (str): Code valute (наприклад, 'USD', 'UAH').

    Returns:
        float: price of one bit_ka in valute.
    """
    response = requests.get('https://bitpay.com/api/rates')
    rates = response.json()
    for rate in rates:
        if rate['code'] == currency:
            return rate['rate']
    raise ValueError(f"Валюта {currency} не знайдена")

