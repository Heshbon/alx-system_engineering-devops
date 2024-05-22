#!/usr/bin/python3
"""Returns information about employees TODO list progress."""
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = base_Url + "/" + employeeId

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    items = response.json()
    done = 0
    done_items = []

    for item in items:
        if item.get('completed'):
            done_items.append(item)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(items)))

    for task in done_items:
        print("\t {}".format(task.get('title')))
