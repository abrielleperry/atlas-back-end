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
    
    
 #   Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
