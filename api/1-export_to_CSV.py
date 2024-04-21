#!/usr/bin/python3
"""
Python module returns information about his/her TODO list progress and exports
it to a CSV file.
"""
import requests
import csv
from sys import argv

if __name__ == '__main__':
    URL = "https://jsonplaceholder.typicode.com"
    user_id = argv[1]
    response = requests.get("{}/users/{}".format(URL, user_id))
    user_data = response.json()

    todo_resp = requests.get("{}/todos?userId={}".format(URL, user_id))
    todo_data = todo_resp.json()

    # Prepare the CSV file
    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = [
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
                ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write task data
        for task in todo_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user_data["username"],
                "TASK_COMPLETED_STATUS": "Completed"
                if task["completed"] else "Not Completed",
                "TASK_TITLE": task["title"]
            })

    print("Data exported to {}".format(csv_filename))
