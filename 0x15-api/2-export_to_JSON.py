#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    tasks = [{
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": username
    } for todo in todos]

    json_data = {str(user_id): tasks}

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(json_data, jsonfile)
