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

def employee_name(users_data, employee_id):
    """ get employee name """
    for user in users_data:
        if user['id'] == employee_id:
            return user['name']
    return None


def count_done_tasks(todos_data, employee_id):
    """ get count of completed tasks for input employee id """
    number_of_done_tasks = sum(
        1 for todo in todos_data
        if todo['userId'] == employee_id and todo['completed'])
    return number_of_done_tasks


def count_total_tasks(todos_data, employee_id):
    """ get count of total tasks for input employee id """
    total_number_of_tasks = sum(1 for todo in todos_data
                                if todo['userId'] == employee_id)
    return total_number_of_tasks


def completed_task_title(todos_data, employee_id):
    """ if task is completed print task title """
    for tasks in todos_data:
        if tasks['userId'] == employee_id and tasks['completed']:
            print(f"\t {tasks['title']}")


if __name__ == "__main__":
    users_data, todos_data = employee_data()
    input_id = int(sys.argv[1])
    name = employee_name(users_data, input_id)
    comp_tasks = count_done_tasks(todos_data, input_id)
    total_tasks = count_total_tasks(todos_data, input_id)

    print(f"Employee {name} is done with tasks({comp_tasks}/{total_tasks}):")
    print(f"\t {completed_task_title(todos_data, input_id)}")
