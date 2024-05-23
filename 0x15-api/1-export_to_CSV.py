#!/usr/bin/python3
"""Extend task #0 python script to export data in the CSV format"""

import requests
import sys
import json
import csv

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
                with open(sys.argv[1] + '.csv', 'w', newline='') as csvfile:
                    write_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                    for todo in todo_l:
                        line = [user_d.get('id'), user_d.get('username'),
                                todo.get('completed'), todo.get('title')]
                        write_file.writerow(line)
