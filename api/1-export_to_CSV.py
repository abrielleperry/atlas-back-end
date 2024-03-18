#!/usr/bin/python3
""" user inputs employee id and task data is returned """
import csv
import requests
import sys


def fetch_employee_data():
    """ get user and todo data from API """
    users_data = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_data = requests.get("https://jsonplaceholder.typicode.com/todos")
    return users_data.json(), todos_data.json()

if __name__ == "__main__":
    users_data, todos_data = fetch_employee_data()
    input_id = int(sys.argv[1])

    """ get user name from users_data """
    for user in users_data:
        if user['id'] == input_id:
            username = user['username']

    with open(f'{input_id}.csv', 'w', newline="") as csvfile:
        employee_csv = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for data in todos_data:
            if data['userId'] == input_id:
                employee_csv.writerow(
                    [input_id, username, data['completed'], data['title']])
