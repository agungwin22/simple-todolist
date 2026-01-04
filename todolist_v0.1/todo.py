# To-Do-List in Python

tasks = []

def show_menu():
    print("--- To Do List ---")
    print("-- Author agungwin22 --")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter Task: ")
    tasks.append({"task": task, "done":False})
    print(f"Task '{task}' Added!")

def view_task():
    if not tasks: # ini adalah erro handling
        print(" ")
        print("="*40)
        print("No tasks yet!")
        print("="*40)
        return
    print("\nYour Tasks: ")
    print("="*40)
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        
        print(f"{index} {task['task']} [{status}]")
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
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("GoodBye!!")
        break
    else:
        print("Enter invalid number. try again!")