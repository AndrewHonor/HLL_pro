from flask import Flask, render_template
from markupsafe import escape
import secrets
import string
import csv
import json

app = Flask(__name__)


@app.route("/admin")
def helo_world():
    return "Heloword_2"


@app.route("/generate_password")
def generate_password():
    ########
    ###     Є СЕРЙОЗНЕ ПИТАННЯ - чому якщо часто і швидко перезавантажувати сторінку
    ###     то інколи генерується пароль довжиною в 3-4 символи ???
    ###     хоча там чітко визначений цикл в 20 ітерацій
    ########
    """
    from 10 to 20 chars
    upper and lower case
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(secrets.choice(alphabet) for _ in range(20))
    print(generated_password)
    return escape(generated_password)


@app.route("/calculate_average")
def calculate_average():
    """
    csv file with students
    1.calculate average high
    2.calculate average weight
    csv - use lib
    *pandas - use pandas for calculating
    """

    def csv_to_list_of_lists(csv_file_path):
        list_of_lists = []
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропустимо перший рядок (заголовки стовпців)
            for row in reader:
                converted_row = [float(cell) for cell in row]
                list_of_lists.append(converted_row)
        return list_of_lists

    csv_file_path = 'hw.csv'
    list_of_lists = csv_to_list_of_lists(csv_file_path)
    total_sum_long = 0
    total_sum_mass = 0
    count = 0
    for x in list_of_lists:
        if len(x) > 2:
            total_sum_long += x[2]
            total_sum_mass += x[1]
            count += 1
    average_long = str(total_sum_long / count)
    average_mass = str(total_sum_mass / count)
    return f"{average_long}, {average_mass}"


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
