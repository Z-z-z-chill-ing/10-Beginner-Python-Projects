import os

def check_empty(line):
    if (len(line) == 0):
        return False
    else:
        return True

def add_func():
    try:
        name = input("What is the name of your to-do list: ")
        title = input("Give a title to a task: ")
        description = input("Give a description to a task: ")
        num_lines = 0
        if (not (name and title and description)):
            raise ValueError("The name, title, and description shouldn't be empty.")
        if (not description[len(description) - 1] == "."):
            description += ".\n"
        else:
            description += "\n"
        if (not os.path.isfile(f"{name}.txt")):
            with open(f"{name}.txt", "w") as file:
                file.close()
        with open(f"{name}.txt", "r") as fread:
            for line in fread:
                num_lines += line.count(".")
            with open(f"{name}.txt", "a") as fwrite:
                formatTask = f"{num_lines + 1}) {title}: {description}"
                fwrite.write(formatTask)
                fwrite.close()
            fread.close()
        print("Task was successfully appended.")
    except ValueError as e:
        print(f"\nError: {e}")

def fetch_func():
    try:
        name = input("What is the name of your to-do list: ")
        if (not name):
            raise ValueError("The name shouldn't be empty.")
        with open(f"{name}.txt", "r") as fread:
            print("\n" + "All of your tasks are here".center(80, "-") + "\n")
            for line in fread:
                print(f"{line[0:len(line) - 1]}")
            print("\n" + "".center(80, "-") + "\n")
            fread.close()
    except ValueError as e:
        print(f"Error: {e}")

def remove_func():
    try:
        name = input("What is the name of your to-do list: ")
        if (not name):
            raise ValueError("The name shouldn't be empty.")
        freadContent = ""
        newContent = ""
        num_lines = 0
        with open(f"{name}.txt", "r") as fread:
            print("\n" + "All of your tasks are here".center(80, "-") + "\n")
            for line in fread:
                num_lines += line.count(".")
                print(f"{line[0:len(line) - 1]}")
            print("\n" + "".center(80, "-") + "\n")
            fread.close()
        indexRemove = input("\nEnter the index of the corresponding task you would like to remove: ")
        if (int(indexRemove) > num_lines):
            raise IndexError(f"There is maximum of {num_lines} tasks.")
        with open(f"{name}.txt", "r") as fread:
            for index, line in enumerate(fread, 1):
                if (not line[0] == indexRemove):
                    freadContent += line
            lines = list(filter(check_empty, freadContent.split("\n")))
            fread.close()
        with open(f"{name}.txt", "w") as fwrite:
            for index, line in enumerate(lines, 0):
                index = str(index + 1)
                if (line[0] == indexRemove):
                    continue
                else:
                    formatTask = index + line[1:] + "\n"
                    newContent += formatTask
            fwrite.write(newContent)
            fwrite.close()
    except (ValueError, IndexError) as e:
        print(f"\nError: {e}")

def update_func():
    try:
        name = input("What is the name of your to-do list: ")
        if (not name):
            raise ValueError("The name shouldn't be empty.")
        with open(f"{name}.txt", "r") as fread:
            print("\n" + "All of your tasks are here".center(80, "-") + "\n")
            for line in fread:
                print(f"{line[0:len(line) - 1]}")
            print("\n" + "".center(80, "-") + "\n")
            fread.close()
        indexUpdate = input("Enter an index of a task you wish to update: ")
        newTitle = input("Give a title to update a task: ")
        newDescription = input("Give a description to update a task: ")
        newContent = ""
        if (not newDescription[len(newDescription) - 1] == "."):
            newDescription += "."
        else:
            newDescription += ""
        tasks = []
        with open(f"{name}.txt", "r") as fread:
            for task in fread:
                tasks.append(task[:-1])
            tasks.pop(int(indexUpdate) - 1)
            fread.close()
        formatTask = f"{indexUpdate}) {newTitle}: {newDescription}"
        tasks.insert(int(indexUpdate) - 1, formatTask)
        for task in tasks:
                newContent += task + "\n"
        with open(f"{name}.txt", "w") as fwrite:
            fwrite.write(newContent)
            fwrite.close()
    except (ValueError) as e:
        print(f"\nError: {e}")

menu = """
1. Append A Task.
2. Fetch All Tasks.
3. Remove A Task.
4. Update A Task
5. Exit.
"""

while True:
    print(menu)
    menuSelect = input("Choose the corresponding number of an action: ")
    if (menuSelect == 5 or menuSelect == "5"):
        os.system("clear")
        break
    elif (menuSelect == 1 or menuSelect == "1"):
        add_func()
    elif (menuSelect == 2 or menuSelect == "2"):
        fetch_func()
    elif (menuSelect == 3 or menuSelect == "3"):
        remove_func()
    elif (menuSelect == 4 or menuSelect == "4"):
        update_func()
    else:
        print("\nInvalid choice.")
        continue
