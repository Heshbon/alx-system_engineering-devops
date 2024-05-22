#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    items = response.json()

    data_structure = {employeeId: []}
    for item in items:
        data_structure[employeeId].append({
            "task": item.get('title'),
            "completed": item.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(data_structure, filename)
