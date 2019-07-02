
import json

class Tasks:
    def __init__(self, name, priority, status = "Incomplete"):
        self.name = name
        self.priority = priority
        self.status = status

    def MakeDict(self):
        new_dict = {
            "name": self.name,
            "priority": self.priority,
            "status": self.status
            }
        return new_dict

def writeJSON():
     with open("ToDoStore.json","w") as file:
        json.dump(taskList,file)
    
def importJSON():
    try:
        with open("ToDoStore.json") as file:
            taskList = json.load(file)
    except json.decoder.JSONDecodeError:
        taskList = []
    return taskList


def GetChoice():
    choice = None
    print("Choose an option:\n1 -- Add Task\n2 -- Modify Task\n3 -- Delete Task\n4 -- View All Tasks\nq -- Quit\n")
    choice = input(">> ")
    while choice != 'q' and choice != 'Q':
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            return choice
        else:
            print("Please select a valid option")
            choice = input(">> ")
    quit()


def Menu():
    print("\n\n......Welcome to Eric's To-Do List......\n")
    choice = GetChoice()
    if choice == "1":
        AddTask()
    elif choice == "2":
        ModifyTask()
    elif choice == "3":
        DeleteTask()
    elif choice == "4":
        ViewTask()
    else: 
        quit()


def AddTask():
    print("\n      ~ADD TASK~       \n")
    name = input("Enter task name: ")
    priority = input("Enter priority (high/med/low): ")
    while priority != "high" and priority != "med" and priority != "low":
        print("Please enter priority as high, med, or low")
        priority = input("Enter priority (high/med/low): ")
    task = Tasks(name,priority)
    taskList.append(task.MakeDict())
    print(f"\nAdded {name} with priority = {priority}.\n")
    writeJSON()
    Menu()

# DELETE FUNCTIONS
def DeleteTask():
    print("\n     ~DELETE TASK~     \n")
    DelViewTask()
    choice, confirm = GetDelChoice()
    if confirm == "y":
        print(taskList[choice]["name"] + " was deleted.")
        del taskList[choice]
    elif confirm == "n":
        print(taskList[choice]["name"] + " was not deleted.")
    writeJSON()
    Menu()
    

def GetDelChoice():
    choice = None
    choice = input("\nChoose a task index to delete, or q to cancel: ")
    try:
        choice = int(choice)
    except:
        while type(choice) != int:
            if choice.lower() == 'q':
                Menu()
            choice = input("\nPlease choose an index in the range 0 - " + str(len(taskList)-1) + ": ")
            try:
                choice = int(choice)
            except:
                pass
    while choice < 0 or choice > (len(taskList) -1):
        choice = int(input("Selected index not in range. Enter index to delete: "))
    confirm = input("\nDelete task " + taskList[choice]["name"] + f" at index {choice}? (y/n): ")
    while confirm != 'y' and confirm != 'n':
        confirm = input("\nEnter (y/n): ")
    return choice, confirm

#Delete menu modification of ViewTask() (by default doesn't offer a return to menu option)

def DelViewTask():
    print("\n.......Task List.......\n")
    try:
        temp = taskList[0]
    except IndexError:
        print("\nYou don't have any tasks yet\n")
        confirm = input("\nPress m to return to menu.\n")
        while confirm != 'm' and confirm != 'M':
            confirm = input("\nPress m to return to menu.\n")
        Menu()
    index = 0
    for task in taskList:
        PrintTask(index,task)
        index +=1

#justify function for PrintTask()

def GetMaxLen(variant):
    if variant == "i":
        maxLen = len(str(len(taskList)))
        maxLen += 2
    else:
        maxLen = len(taskList[0][variant])
        for i in taskList:
            if len(i[variant]) > maxLen:
                maxLen = len(i[variant])
        maxLen += 3
    return maxLen

def PrintTask(index, task):
    maxIndex = GetMaxLen("i")
    maxName = GetMaxLen("name")
    maxPri = GetMaxLen("priority")
    index_space = "-" * (maxIndex - len(str(index)))
    task_space ="-" * (maxName - len(task["name"]))
    pri_space ="-" * (maxPri - len(task["priority"]))
    print(f'{str(index)} {index_space} {str(taskList[index]["name"])} {task_space} {str(taskList[index]["priority"])} {pri_space} {str(taskList[index]["status"])}')


def ViewTask():
    print("\n.......Task List.......\n")
    try:
        temp = taskList[0]
    except IndexError:
        print("\nYou don't have any tasks yet\n")
    index = 0
    for task in taskList:
        PrintTask(index,task)
        index +=1
    confirm = input("\nPress m to return to menu.\n")
    while confirm != 'm' and confirm != 'M':
        confirm = input("\nPress m to return to menu.\n")
    Menu()



#  MODIFY FUNCTIONS
def ModifyTask():
    print("\n     ~MODIFY TASK~     \n")
    DelViewTask()
    choice = GetModChoice()
    option = GetModOption()
    if option == "1":
        ModName(choice)
    elif option == "2":
        ModPri(choice)
    elif option == "3":
        ModStat(choice)
    


def GetModChoice():
    choice = None
    choice = input("\nChoose a task index to modify, or q to cancel: ")
    try:
        choice = int(choice)
    except:
        while type(choice) != int:
            if choice.lower() == 'q':
                Menu()
            choice = input("\nPlease choose an index in the range 0 - " + str(len(taskList)-1) + ": ")
            try:
                choice = int(choice)
            except:
                pass
    while choice < 0 or choice > (len(taskList) -1):
        choice = int(input("Selected index not in range. Enter index to modify: "))
    print("\nModifying " + taskList[choice]["name"])
    return choice

def GetModOption():
    option = None
    print("What would you like to modify?\n\n1 -- Task Name\n2 -- Task Priority\n3 -- Task Status\nb -- Back\nm -- Main Menu")
    option = input(">>")
    while option != 'b' and option != 'B' and option != 'm' and option != 'M':
        if option == "1" or option == "2" or option == "3":
            return option
        else:
            option = input("Please select a valid option: ")
    if option == 'b' or option == 'B':
        ModifyTask()
    else:
        Menu

def ModName(choice):
    newName = input("Enter new name: ")
    taskList[choice]["name"] = newName
    writeJSON()
    ModifyTask()

def ModPri(choice):
    newPri = input("Enter new priority (high/med/low): ")
    while newPri != "high" and newPri != "med" and newPri != "low":
        print("Please enter priority as high, med, or low")
        newPri = input("Enter new priority (high/med/low): ")
    taskList[choice]["priority"] = newPri
    writeJSON()
    ModifyTask()

def ModStat(choice):
    if taskList[choice]["status"] == "Incomplete":
        confirm = input("Mark " + taskList[choice]["name"] + " as Complete? (y/n): ")
        while confirm != 'y' and confirm != 'Y' and confirm != 'n' and confirm != 'N':
            confirm = input("\nEnter (y/n): ")
        if confirm == 'y':
            taskList[choice]["status"] = "Complete"
            print(taskList[choice]["name"] + " completed.")
        elif confirm == 'n':
            print("Changes not saved")
    else:
        confirm = input("Mark " + taskList[choice]["name"] + " as Incomplete? (y/n): ")
        while confirm != 'y' and confirm != 'Y' and confirm != 'n' and confirm != 'N':
            confirm = input("\nEnter (y/n): ")
        if confirm == 'y':
            taskList[choice]["status"] = "Incomplete"
            print("Changes Saved.")
        elif confirm == 'n':
            print("Changes not saved.")
    writeJSON()
    ModifyTask()
        




taskList = importJSON()
Menu()

