# Name: Dat , ID: 100886108

from datetime import datetime

def addNewItem():
    global ToDoList

    while True:
        UserTask = input("Please enter a task: ")
        if checkItemExists(UserTask):
            print("Task already exists! Select the option again ")
        else: 
            Now = datetime.now()
            while True:
                Deadline = input("Please enter the deadline: (yyyy/mm/dd HH:MM:SS) ")
                ConvertedDeadline = datetime.strptime(Deadline, "%Y/%m/%d %H:%M:%S")   
                if ConvertedDeadline <= Now:
                    print("Time entered is in the past! Select the option again")
                    break
                else:
                    ToDoList.append((UserTask, Deadline))
                    print("Task added successfully!")
                    break
        break
    
    ToDoList.sort(key=takeSecond)

def checkItemExists(taskName):
    global ToDoList

    for i in ToDoList:
        if taskName in i:
            return True
    return False

def takeSecond(element):
    return element[1]

def printListItems():
    global ToDoList
    
    for x, y in enumerate(ToDoList):
        print(f"{x}. {y[0]} - {y[1]}")

def removeListItems():
    global ToDoList
    LengthToDoList = len(ToDoList)
    printListItems()
    DeleteItems = int(input(f"Which task would you like to delete ? (0-{LengthToDoList - 1}): "))
    del ToDoList[DeleteItems]
    print("Removed successfully!")

ToDoList = []

while True:
    UserSelection = int(input("Options:\n 1. Enter a new To do item\n 2. Print the list of all To do items\n 3. Remove a To do item\n 4. Exit the program\n Your choice: "))
    if UserSelection == 1:
        addNewItem()
    elif UserSelection == 2:
        printListItems()
    elif UserSelection == 3:
        removeListItems()
    elif UserSelection == 4:
        print("Exit!")
        break
    else:
        print("Please enter from 1-4!")
    
