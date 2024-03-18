#!/usr/bin/python3
""" user inputs employee id and task data is returned """
import csv
import json
import requests
import sys


def fetch_employee_data():
    """ get user and todo data from API """
    users_data = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_data = requests.get("https://jsonplaceholder.typicode.com/todos")
    return users_data.json(), todos_data.json()


if __name__ == "__main__":
    users_data, todos_data = fetch_employee_data()

    info = {}
    with open(f'todo_all_employees.json', 'w', newline="") as jsonfile:
        for user in users_data:
            input_id = user['id']
            username = user['username']
            info[input_id] = []

        for data in todos_data:
            if data['userId'] in info:
                info[data['userId']].append({
                    "username": username,
                    "task": data['title'],
                    "completed": data['completed']
                })

        for user in users_data:
            input_id = user['id']
            if input_id not in info:
                info[input_id] = []

        json.dump(info, jsonfile)
