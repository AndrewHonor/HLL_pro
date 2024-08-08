from flask import Flask, request, render_template_string
########
####    Скажу через цю бібліотечку швидше. один мінус, у ній не має значка гривні.
####    Ghjcnj gbit UAH
########
# from forex_python.converter import CurrencyCodes
from faker import Faker
import csv
import json
import requests

app = Flask(__name__)
fake = Faker()


def generate_students(num_students=100):
    """
    Generator of students

    Args:
        num_students (int): Number of students to generate.

    Returns:
        list: List of dictionaries with student data.

    Raises:
        ValueError: Якщо кількість студентів перевищує 1000.
    """
    if num_students > 1000:
        raise ValueError("Кількість студентів не може перевищувати 1000")

    students = []
    for _ in range(num_students):
        student = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(),
            "birthday": fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%Y-%m-%d")
        }
        students.append(student)

    return students


def save_students_to_csv(students, filename='students.csv'):
    """
    Saves the list to a CSV file.

    Args:
        students (list):
        filename (str):
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "email", "password", "birthday"])
        writer.writeheader()
        writer.writerows(students)


def get_currency_symbols():
    """
    Gets symbols of all #valut# з BitPay API.

    Returns:
        dict: Dictionary codes.
    """
    response = requests.get('https://test.bitpay.com/currencies')
    data = response.json()
    symbols = {currency['code']: currency['symbol'] for currency in data['data']}
    return symbols


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