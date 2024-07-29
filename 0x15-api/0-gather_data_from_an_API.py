#!/usr/bin/python3
"""Returns information about the to-do list for a given employee ID."""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = "https://jsonplaceholder.typicode.com/"
        user_resp = requests.get(url + 'users/{}'.format(sys.argv[1]))
        todo_resp = requests.get(url + 'todos?userId={}'.format(sys.argv[1]))
        if all([user_resp, todo_resp]) is not None:
            try:
                user_d = json.loads(user_resp.text)
            except JSONDecodeError:
                user_d = {}
            try:
                todo_l = json.loads(todo_resp.text)
            except JSONDecodeError:
                todo_l = []
            tasks = ''
            completed = 0
            total = 0
            if type(todo_l) is list:
                for todo in todo_l:
                    if type(todo) is not dict:
                        continue
                    if todo.get('completed') is True:
                        tasks += '\t {}\n'.format(todo.get('title'))
                        completed += 1
                total = len(todo_l)
            if type(user_d) is dict and user_d != {}:
                emp_Id = 'Employee {} is done with tasks({}/{}):\n'\
                    .format(user_d.get('name'), completed, total)
                print(emp_Id + tasks, end='')
