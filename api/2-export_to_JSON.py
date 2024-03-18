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
    input_id = int(sys.argv[1])

    """ get user name from users_data """
    for user in users_data:
        if user['id'] == input_id:
            username = user['username']
    info = {}
    info[input_id]= []

    with open(f'{input_id}.json', 'w', newline="") as jsonfile:
        for data in todos_data:
            if data['userId'] == input_id:
                info[input_id].append({
                    "task": data['title'],
                    "completed": data['completed'], 
                    "username": username
                })    
        json.dump(info, jsonfile) 
