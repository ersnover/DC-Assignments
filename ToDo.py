
class Tasks:
    def __init__(self, name, priority, status = "Incomplete"):
        self.name = name
        self.priority = priority
        self.status = status


    

def GetChoice():
    choice = None
    print("Choose an option:\n1 -- Add Task\n2 -- Modify Task\n3 -- Delete Task\n4 -- View All Tasks\nq -- Quit")
    choice = input(">> ")
    while choice != 'q' and choice != 'Q':
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            return choice
        else:
            print("Please select a valid option")
            choice = input(">> ")
    quit()

def TaskListInit():
    taskList = []
    return taskList

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
    index = len(taskList)
    taskList.append(Tasks(name,priority))
    print("\nAdded " + taskList[index].name + f" with priority = {priority}.\n")
    Menu()

# DELETE FUNCTIONS
def DeleteTask():
    print("\n     ~DELETE TASK~     \n")
    DelViewTask()
    choice, confirm = GetDelChoice()
    if confirm == "y":
        print(taskList[choice].name + " was deleted.")
        del taskList[choice]
    elif confirm == "n":
        print(taskList[choice].name + " was not deleted.")
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
    confirm = input("\nDelete task " + taskList[choice].name + f" at index {choice}? (y/n): ")
    while confirm != 'y' and confirm != 'n':
        confirm = input("\nEnter (y/n): ")
    return choice, confirm

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
        print(f"{index} - " + taskList[index].name + " --- " + taskList[index].priority + " --- " + taskList[index].status)
        index +=1


def ViewTask():
    print("\n.......Task List.......\n")
    try:
        temp = taskList[0]
    except IndexError:
        print("\nYou don't have any tasks yet\n")
    index = 0
    for task in taskList:
        print(f"{index} - " + taskList[index].name + " --- " + taskList[index].priority + " --- " + taskList[index].status)
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
    return choice

def GetModOption():
    option = None
    print("\nWhat would you like to modify?\n1 -- Task Name\n2 -- Task Priority\n3 -- Task Status\nb -- Back\nm -- Main Menu")
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
    taskList[choice].name = newName
    ModifyTask()

def ModPri(choice):
    newPri = input("Enter new priority (high/med/low): ")
    while newPri != "high" and newPri != "med" and newPri != "low":
        print("Please enter priority as high, med, or low")
        newPri = input("Enter new priority (high/med/low): ")
    taskList[choice].priority = newPri
    ModifyTask()

def ModStat(choice):
    newStat = input("Enter new status (I/C): ")
    while newStat != "i" and newStat != "I" and newStat != "c" and newStat != "C":
        print("Please enter status as I for Incomplete or C for Complete")
        newStat = input("Enter new status (I/C): ")
    if newStat.lower() == "i":
        taskList[choice].status = "Incomplete"
    elif newStat.lower() == "c":
        taskList[choice].status = "Complete"
    ModifyTask()




# run = Tasks('run', 'high')
# mow = Tasks('mow', 'med')
# groceries = Tasks('groceries', 'low')

# taskList = [run, mow, groceries]
taskList = TaskListInit()
Menu()

