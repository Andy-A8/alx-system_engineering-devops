#!/usr/bin/python3
"""Extends information of all employees to JSON format"""

import collections
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_resp = requests.get(url + "users")
    users_todo_d = collections.OrderedDict()
    if users_resp is not None:
        try:
            users_l = json.loads(users_resp.text)
        except JSONDecodeError:
            users_l = []
        if type(users_l) is list:
            with open('todo_all_employees.json', 'w') as jsonfile:
                for user_d in users_l:
                    if type(user_d) is not dict:
                        continue
                    user_id = str(user_d.get('id'))
                    username = user_d.get('username')
                    if user_id == 'None':
                        continue
                    todo_resp = requests.get(url + 'todos?userId={}'
                                             .format(user_id))
                    if todo_resp is None:
                        continue

                    try:
                        todo_l = json.loads(todo_resp.text)
                    except JSONDecodeError:
                        todo_l = []
                    if type(todo_l) is not list:
                        continue
                    alt_todo_l = []
                    for todo in todo_l:
                        if type(todo) is not dict:
                            continue
                        todo_d = collections.OrderedDict()
                        todo_d["username"] = username
                        todo_d["task"] = todo.get('title')
                        todo_d["completed"] = todo.get('completed')
                        alt_todo_l.append(todo_d)
                    users_todo_d[user_id] = alt_todo_l
                json.dump(users_todo_d, jsonfile)
