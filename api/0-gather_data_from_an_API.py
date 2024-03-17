#!/usr/bin/python3
from flask import request
import sys

def employee_data():
    users_data = request.get("https://jsonplaceholder.typicode.com/users")
    todos_data = request.get("https://jsonplaceholder.typicode.com/todos")
    return users_data.json(), todos_data.json()

    
def employee_name(users_data, employee_id):
    for user in users_data:
        if user['id'] == employee_id:
            return user['name']
    return None

def count_done_tasks(todos_data, employee_id):
    number_of_done_tasks = sum(1 for todo in todos_data 
                     if todo['userId'] == employee_id)
    return number_of_done_tasks

def count

if __name__ == "__main__":
    users_data, todos_data = employee_data()
input_id = int(sys.argv[1])
name = 

if name:
    print(f"Employee {name} is done with tasks({/}).")
else:
    
    Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):
