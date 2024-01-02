#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
Return information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import requests
    import sys

    DONE_TASKS = 0
    ALL_TASKS = 0

    URL_FOR_USERS = "https://jsonplaceholder.typicode.com/users/{0}".\
        format(sys.argv[1])
    URL_FOR_TODOS = "https://jsonplaceholder.typicode.com/todos"
    R_FOR_USERS = requests.get(URL_FOR_USERS)
    R_FOR_TODOS = requests.get(URL_FOR_TODOS)

    user = R_FOR_USERS.json().get("user")
    todos = R_FOR_TODOS.json()
    for todo in todos:
        if todo.get("userId") == int(sys.argv[1]):
            ALL_TASKS += 1
        if (todo.get("userId") == int(sys.argv[1]))\
                and (todo.get("completed")):
            DONE_TASKS += 1
    print("Employee {} is done with tasks({}/{}:".
        format(user, DONE_TASKS, ALL_TASKS))
    for todo in todos:
        if (todo.get("userId") == int(sys.argv[1]))\
                and (todo.get('completed')):
            print("\t {}".format(todo.get('title')))
