#!/usr/bin/python3
"""
Export data in JSON format
Record all tasks from all employees
"""
if __name__ == "__main__":
    import requests
    import json

    FILENAME = 'todo_all_employees.json'
    URL_FOR_USERS = 'https://jsonplaceholder.typicode.com/users'
    URL_FOR_TODOS = 'https://jsonplaceholder.typicode.com/todos'

    R_FOR_USERS = requests.get(URL_FOR_USERS)
    R_FOR_TODOS = requests.get(URL_FOR_TODOS)

    users = R_FOR_USERS.json()
    todos = R_FOR_TODOS.json()
    todo_all_employees = {}

    for user in users:
        todos_list = []
        for todo in todos:
            if todo.get("userId") == user.get("id"):
                my_dict = {"username": user.get("username"),
                        "task": todo.get("title"),
                        "completed": todo.get("completed")}
                todos_list.append(my_dict)
        todo_all_employees[user.get("id")] = todos_list
    with open(FILENAME, 'w+') as f:
        json.dump(todo_all_employees, f)
