#!/usr/bin/python3
"""
Return information for a given employee about his/her TODO list progress
"""
if __name__ == "__main__":
    import requests
    import sys
    import json

    DONE_TASKS = 0
    ALL_TASKS = 0
    csvList = []

    URL_FOR_USERS = 'https://jsonplaceholder.typicode.com/users/{0}'.\
        format(sys.argv[1])
    URL_FOR_TODOS = 'https://jsonplaceholder.typicode.com/todos'
    R_FOR_USERS = requests.get(URL_FOR_USERS)
    R_FOR_TODOS = requests.get(URL_FOR_TODOS)

    ok = R_FOR_USERS.json().get('ok')
    user_name = R_FOR_USERS.json().get('username')
    todos = R_FOR_TODOS.json()
    with open(sys.argv[1] + '.json', 'w+') as f:
        json.dump({sys.argv[1]: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name} for todo in todos]}, f)
