#!/usr/bin/python3
""" user inputs employee id and task data is returned """
import json
import requests


def fetch_employee_data():
    """ get user and todo data from API """
    users_data = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_data = requests.get("https://jsonplaceholder.typicode.com/todos")
    return users_data.json(), todos_data.json()


if __name__ == "__main__":
    users_data, todos_data = fetch_employee_data()

    info = {}
    usernames = {user['id']: user['username'] for user in users_data}
    with open(f'todo_all_employees.json', 'w', newline="") as jsonfile:
        for user_id, username in usernames.items():
            info[user_id] = {'username': username, 'todos': []}

        for data in todos_data:
            if data['userId'] in info:
                info[data['userId']]['todos'].append({
                    "task": data['title'],
                    "completed": data['completed']
                })

        json.dump(info, jsonfile)
