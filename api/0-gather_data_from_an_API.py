#!/usr/bin/python3
"""
Python module returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("UsageError: python3 {} employee_id(int)".format(__file__))
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"
    EMP_ID = int(sys.argv[1]) # Convert EMP_ID to integer

    try:
        response = requests.get(
            "{}/users/{}/todos".format(URL, EMP_ID),
            params={"_expand": "user"}
        )
        response.raise_for_status() # Raise an exception if the request failed
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        sys.exit(1)
    except Exception as err:
        print(f'Other error occurred: {err}')
        sys.exit(1)

    data = response.json()

    emp_name = data[0]["user"]["name"]
    total_tasks = len(data)
    done_tasks = [task for task in data if task["completed"]]
    total_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks".format(emp_name),
          "({}/{}):".format(total_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task['title']))
