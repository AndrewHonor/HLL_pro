from flask import Flask, request, render_template_string
from faker import Faker
import csv
import json

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

def get_bitcoin_value():
    # https://bitpay.com/api/rates
    # /bitcoin_rate?currency=UAH&convert=100
    # input parameter currency code
    # default is USD
    # default count is 1
    # return value currency of bitcoin
    # add one more input parameter count and multiply by currency (int)
    # * https://bitpay.com/api/
    # * Example: $, €, ₴
    # * return symbol of input currency code
    pass


if __name__ == '__main__':
    app.run(debug=True)
