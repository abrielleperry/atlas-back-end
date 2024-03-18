#!/usr/bin/python3
""" user inputs employee id and task data is returned """
import requests
import sys
import csv

def fetch_employee_data():
    """ get user and todo data from API """
    users_data = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_data = requests.get("https://jsonplaceholder.typicode.com/todos")
    return users_data.json(), todos_data.json()

users_data, todos_data = fetch_employee_data()
input_id = int(sys.argv[1])

""" get user name from users_data """
for user in users_data:
    if user['id'] == input_id:
        username = user['username']

with open({input_id}, 'w', newline="") as csvfile:
    
