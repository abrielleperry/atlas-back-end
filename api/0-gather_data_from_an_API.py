#!/usr/bin/python3
from flask import request
import sys

def employee_data():
    employee_user = request.get("https://jsonplaceholder.typicode.com/users")
    employee_todo = request.get("https://jsonplaceholder.typicode.com/todos")
    return employee_user.json(), employee_todo.json()

    
def employee_name(employee_user, input_id):
    for user in employee_user:
        if user['id'] == input_id:
            return user['name']
    return None

def todo_progress(employee_todo, input_id):
    


if __name__ == "__main__":
    employee_name, employee_todo = employee_data()
input_id = int(sys.argv[1])
name = 
