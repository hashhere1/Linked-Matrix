import os

"""File Handling"""

# Creating a file
if os.path.exists("sample.txt"):
    pass
else:
    with open("sample.txt", "x") as file:
        pass



# Writing into a file
with open("sample.txt", "w") as file:
    file.write(input("What do you want to write into the file? "))

# Appending into a file
with open("sample.txt", "a") as file:
    file.write("\nAppending into the file.")


# Reading from a file
if os.path.exists("sample.txt"):
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
else:
    print("No file exists")

"""To Do list"""

print("\n To Do list")
filename = "todo.txt"

def add_task():
    task = input("Enter a task: ")
    with open(filename, "a") as file:
        file.write(task + "\n")
    print("Task added.\n")

def show_tasks():
    try:
        with open(filename, "r") as file:
            print("\nYour Tasks:")
            print(file.read())
    except FileNotFoundError:
        print("\nNo tasks found.\n")

while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")



