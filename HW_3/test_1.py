from flask import Flask, request, render_template_string
########
####    Скажу через цю бібліотечку швидше. один мінус, у ній не має значка гривні.
####    Ghjcnj gbit UAH
########
# from forex_python.converter import CurrencyCodes
from faker import Faker
from mehanic import *
import csv
import json
import requests

app = Flask(__name__)
fake = Faker()


# currency_codes = CurrencyCodes()



@app.route('/generate_students')
def generate_students_route():
    """
    html a page with a table of students

    Returns:
        str: table of students.
    """
    num_students = int(request.args.get('num_students', 111))
    try:
        students = generate_students(num_students)
        save_students_to_csv(students)
        return render_template_string("""
        <table border="1">
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
                <th>Password</th>
                <th>Birthday</th>
            </tr>
            {% for student in students %}
            <tr>
                <td>{{ student.first_name }}</td>
                <td>{{ student.last_name }}</td>
                <td>{{ student.email }}</td>
                <td>{{ student.password }}</td>
                <td>{{ student.birthday }}</td>
            </tr>
            {% endfor %}
        </table>
        """, students=students)
    except ValueError as e:
        return str(e), 400


@app.route('/get_bitcoin_value')
def get_bitcoin_value_route():
    """
    Returns:
        str:
    """
    count = float(request.args.get('count', 1))
    currency = request.args.get('valuta', 'USD')
    try:
        rate = get_bitcoin_value(currency)
        total_value = count * rate
        symbols = get_currency_symbols()
        currency_symbol = symbols.get(currency, currency)
        return f"{total_value:.2f} {currency_symbol}"
    except ValueError as e:
        return str(e), 400


if __name__ == '__main__':
    app.run(debug=True)
