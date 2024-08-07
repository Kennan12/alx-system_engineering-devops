#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her
'''

if __name__ == '__main__':
    
    import requests
    import sys
    import json
    
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    USER_ID = sys.argv[1]
    req = requests.get('https://jsonplaceholder.typicode.com/user/{}'.
                       format(USER_ID)).json()
    USERNAME = req.get("username")
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(USER_ID)).json()
    for item in req:
        if item.get('completed') is True:
            TASK_TITLE.append(item.get('title'))
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS = len(req)

    print('Employee {} is done with tasks{}/{}:'.
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for title in TASK_TITLE:
        print('\t {}'.format(title))
