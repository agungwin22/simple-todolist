# To-Do-List in Python
import os

tasks = []

def show_menu():
    print("="*40)
    print(f"{'--- To Do List ---':^40}")
    print(f"{'-- Author agungwin22 --':^40}")
    print("="*40)
    print(" [1] \tAdd Task\n")
    print(" [2] \tView Task\n")
    print(" [3] \tMark Task as Done\n")
    print(" [4] \tDelete Task")

def add_task():
    print("-"*40)
    task = input("Enter Task: ")
    print("-"*40)
    tasks.append({"task": task, "done":False})
    print(f'\nTask "{task}" Added!')

def view_task():
    if not tasks: # ini adalah erro handling
        print(" ")
        print("="*40)
        print("No tasks yet!")
        print("="*40)
        return
    print("\nYour Tasks: ")
    print("="*40)
    print(f"    No.\t\tTasks\t\tMark")
    print("-"*40)
    for index, task in enumerate(tasks, start=1):
        status = "V" if task["done"] else "X"
        print(f"    [{index}] \t{task['task']} \t[{status}]")
    print("="*40)

def mark_done():
    view_task()
    if not tasks: # error handling
        return
    try:
        index = int(input("Enter task number to mark done: "))
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print("Mark is done!")
        else:
            print("Invalid Number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_task()
    if not tasks: # error handling
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            remove = tasks.pop(index)
            print(f"Deleted Task: {remove['task']}")
        else:
            print("Enter valid number!")
    except ValueError:
        print("Please enter a valid number.")


while True:

    # membuat clear untuk CLI
    os.system("cls")
    # os.system("clear")

    show_menu()
    print("="*40)
    choice = input("\nChoose an option : ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    else:
        print("Enter invalid number. try again!")

    # untuk konfirmasi user
    isdone = input("\nLanjut ? (y/n) : ")

    if isdone == 'n':
        break
