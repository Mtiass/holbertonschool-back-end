#!/usr/bin/python3
"""
Python module returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    URL = "https://jsonplaceholder.typicode.com"
    response = requests.get("{}/users/{}".format(URL, argv[1]))
    user = user_response.json()

    todo_resp = requests.get("{}/todos?userId={]}".format(URL, argv[1]))
    todo_data = todo_resp.json()

    completed = [task for task in todo_data if task["completed"]]

    emp_name = user_data["name"]
    taskcom_num = len(completed)
    total_tasks = len(todo_data)
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, taskcom_num, total_tasks))

    for task in completed:
        print("\t {}".format(task['title']))
