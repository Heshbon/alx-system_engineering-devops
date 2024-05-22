#!/usr/bin/python3
"""Returns information about employees TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = []
    for todo in todos:
        if todo["completed"]:
            completed_tasks.append(todo["title"])

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    for task_title in completed_tasks:
        print("\t{}".format(task_title))
