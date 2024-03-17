#!/usr/bin/python3
from flask import Flask, request
import sys

def employee():
    user = request.get("https://jsonplaceholder.typicode.com/users")
    todo = request.get("https://jsonplaceholder.typicode.com/todos")
