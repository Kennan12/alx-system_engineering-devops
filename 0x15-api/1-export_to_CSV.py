#!/usr/bin/python3
"""
Return information for a given employee about his/her TODO list progress
"""
if __name__ == "__main__":
    import requests
    import sys
    import csv

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
    for todo in todos:
        if todo.get("userId") == int(sys.argv[1]):
            subcsvList = []
        if todo.get("userId") == int(sys.argv[1]):
            ALL_TASKS += 1
            subcsvList.append(todo.get('userId'))
            subcsvList.append(user_name)
            subcsvList.append(todo.get('completed'))
            subcsvList.append(todo.get('title'))
            csvList.append(subcsvList)
        if (todo.get('userId') == int(sys.argv[1]))\
                and (todo.get('completed')):
            DONE_TASKS += 1
    with open(sys.argv[1] + '.csv', 'w+', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(csvList)
