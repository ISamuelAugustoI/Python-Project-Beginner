"""
Author: Samuel Augusto
Date: 22/12/2024
Description: Código que simula um gerenciador de tarefas
"""
def add_task(tasks):
    task = str(input('Enter the task: '))
    tasks.append({'name': task,"complete": False})
    print(f'Task added: {task}')
def list_tasks(tasks):
    print(f'tasks in progress:')
    for i,j in enumerate(tasks):
        status = '✔️' if j['complete'] else '❌'
        print(f'{i+1} - {j['name']} : {status}')
def complete_task(tasks):
    list_tasks(tasks)
    index = int(input('Enter how many task as complete: '))-1
    if(0<=index<len(tasks)):
        tasks[index]['complete'] = True
        print(f'Task complete: {tasks[index]['name']}')
    else:
        print(f'Task invalid.')
def delete_task(tasks):
    list_tasks(tasks)
    index = int(input('Enter how many task as delete: '))-1
    if(0<=index<len(tasks)):
        remove = tasks.pop(index)
        print(f'Delete Task: {remove['name']}')
    else:
        print(f'Task invalid.')
tasks = []
while True:
    print(f'============================')
    print(f'Welcome to the Task Manager:')  
    print(f'[1] = Add Task\n[2] = List Tasks\n[3] = Complete Task\n[4] = Delete Task\n[5] = Exit')
    choice = int(input('Enter your choice: '))
    if(choice==1):
        add_task(tasks)
    elif(choice==2):
        list_tasks(tasks)
    elif(choice==3):
        complete_task(tasks)
    elif(choice==4):
        delete_task(tasks)
    elif(choice==5):
        print(f'Thank you. Good bye!')
        break
    else:
        print(f'Enter the number between 1 and 5...')