#!/usr/bin/python3
"""Extend task #0 python script to export data in the JSON format"""

import collections
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = "https://jsonplaceholder.typicode.com/"
        user_resp = requests.get(url + 'users/{}'.format(sys.argv[1]))
        todo_resp = requests.get(url + 'todos?userId={}'.format(sys.argv[1]))
        user_d = {}
        todo_l = []

        if all([user_resp, todo_resp]) is not None:
            try:
                user_d = json.loads(user_resp.text)
                todo_l = json.loads(todo_resp.text)
            except JSONDecodeError:
                pass
            if type(todo_l) is list and type(user_d) is dict and user_d != {}:
                with open(sys.argv[1] + '.json', 'w') as jsonfile:
                    alt_todo_l = []
                    for todo in todo_l:
                        todo_d = collections.OrderedDict()
                        todo_d['task'] = todo.get('title')
                        todo_d['completed'] = todo.get('completed')
                        todo_d['username'] = user_d.get('username')
                        alt_todo_l.append(todo_d)
                    json.dump({sys.argv[1]: alt_todo_l}, jsonfile)
