#!/usr/bin/python3
"""Export data in the JSON format.
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'
    resp_todos = requests.get(url_todo.format(user_id))
    resp_user = requests.get(url_user.format(user_id))
    json_r_todos = resp_todos.json()
    json_r_user = resp_user.json()

    user_name = json_r_user.get("username")

    json_fname = user_id + ".json"

    val_l = []
    for task in json_r_todos:
        del task["userId"]
        del task["id"]
        task["task"] = task.pop("title")
        task["username"] = user_name
        val_l.append(task)
    dic = {str(user_id): val_l}

    with open(json_fname, 'w+') as fd_json:
        json.dump(dic, fd_json)
