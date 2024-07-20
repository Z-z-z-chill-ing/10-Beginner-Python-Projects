import os
from prettytable import PrettyTable

completeMark = "Done"
uncompleteMark = "Not done"

def string_to_prettytable_update(tableStr, indexUpdate, taskName, taskDescription, timeInterval, completeness):
    lines = tableStr.strip().split("\n")
    data_lines = [line for line in lines if not line.startswith("+")]
    columns = [col.strip() for col in data_lines[0].split("|") if col.strip()]
    prettyTable = PrettyTable(columns)
    for index, line in enumerate(data_lines[1:], 1):
        row = [item.strip() for item in line.split("|") if item.strip()]
        if (row and index == int(indexUpdate)):
            if (taskName): row[0] = taskName
            if (taskDescription): row[1] = taskDescription
            if (timeInterval): row[2] = timeInterval
            if (completeness): row[3] = completeness
        prettyTable.add_row(row)
    return prettyTable

def string_to_prettytable_remove(tableStr, indexRemove):
    lines = tableStr.strip().split("\n")
    data_lines = [line for line in lines if not line.startswith("+")]
    data_lines.pop(int(indexRemove))
    columns = [col.strip() for col in data_lines[0].split("|") if col.strip()]
    prettyTable = PrettyTable(columns)
    for line in data_lines[1:]:
        row = [item.strip() for item in line.split("|") if item.strip()]
        if (row):
            prettyTable.add_row(row)
    return prettyTable

def string_to_prettytable_add(tableStr):
    lines = tableStr.strip().split('\n')
    data_lines = [line for line in lines if not line.startswith('+')]
    columns = [col.strip() for col in data_lines[0].split('|') if col.strip()]
    table = PrettyTable(columns)
    for line in data_lines[1:]:
        row = [item.strip() for item in line.split('|') if item.strip()]
        if row:
            table.add_row(row)
    return table

def add_func():
    listName = input("Enter the [name/date] of your to-do list: ")
    taskName = input("Enter a name of a task: ")
    taskDescription = input("Enter a description of a task: ")
    timeInterval = input("Enter the time interval of a task: ")
    if (not os.path.isfile(f"{listName}.txt")):
        with open(f"{listName}.txt", "w") as file:
            file.close()
    if (os.stat(f"{listName}.txt").st_size == 0):
        table = PrettyTable()
        table.field_names = ["Name", "Description", "Time Interval", "Completeness"]
        table.add_row([taskName, taskDescription, timeInterval, uncompleteMark])
        with open(f"{listName}.txt", "a") as fappend:
            fappend.write(str(table))
            fappend.close()
    else:
        table = ""
        with open(f"{listName}.txt", "r") as fread:
            table = fread.read().strip()
            fread.close()
        prettyTable = string_to_prettytable_add(table)
        prettyTable.add_row([taskName, taskDescription, timeInterval, uncompleteMark])
        with open(f"{listName}.txt", "w") as fwrite:
            fwrite.write(str(prettyTable))
            fwrite.close()
        print(prettyTable)

def fetch_func():
    listName = input("Enter the [name/date] of your to-do list: ")
    with open(f"{listName}.txt", "r") as fread:
            table = fread.read().strip()
            print(table)
            fread.close()

def remove_func():
    listName = input("Enter the [name/date] of your to-do list: ")
    indexRemove = input("Enter the index of task you wish to delete: ")
    table = ""
    with open(f"{listName}.txt", "r") as fread:
        table = fread.read().strip()
        fread.close()
    prettyTable = string_to_prettytable_remove(table, indexRemove)
    with open(f"{listName}.txt", "w") as fwrite:
            fwrite.write(str(prettyTable))
            fwrite.close()


def update_func():
    listName = input("Enter the [name/date] of your to-do list: ")
    indexUpdate = input("Enter the index of task you wish to update: ")
    taskName = input("Enter a new name of a task to update/skip if you don't want to update a name: ")
    taskDescription = input("Enter a new description of a task to update/skip if you don't want to update a description: ")
    timeInterval = input("Enter a new time interval of a task to update/skip if you don't want to update a time interval: ")
    completeness = input("Enter whether you completed a task or not[y/n]/skip if you don't want to update completeness: ")
    table = ""
    with open(f"{listName}.txt", "r") as fread:
        table = fread.read().strip()
        fread.close()
    if (completeness.lower() == "y"):
        completeness = completeMark
    else:
        completeness = uncompleteMark
    prettyTable = string_to_prettytable_update(table, indexUpdate, taskName, taskDescription, timeInterval, completeness)
    with open(f"{listName}.txt", "w") as fwrite:
        fwrite.write(str(prettyTable))
        fwrite.close()

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
    while (not menuSelect.strip().isnumeric() or not menuSelect):
        print("You shouldn't leave this field empty, and it should only contain number [1-5].")
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
