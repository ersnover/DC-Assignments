ToDo = []
ToDo = [
    {"name": "mow", "priority": "high"},
    {"name": "beer", "priority": "med"},
    {"name": "buy food", "priority": "med"},
    {"name": "checkers", "priority": "low"}
]


def GetChoice():
    print("Choose an option:\n1 -- Add Task\n2 -- Delete Task\n3 -- View All Tasks\nq -- Quit")
    choice = input(">> ")
    while choice != 'q' and choice != 'Q':
        if choice == "1" or choice == "2" or choice == "3":
            return choice
        else:
            print("Please select a valid option")
            GetChoice()
    quit()


def Menu():
    print("\n\n......Welcome to Eric's Sweet Ass To-Do List......\n")
    choice = GetChoice()
    if choice == "1":
        AddTask()
    elif choice == "2":
        DeleteTask()
    elif choice == "3":
        ViewTask()
    else: 
        quit()


def AddTask():
    print("\n~ADD TASK~\n")
    name = input("Enter task name: ")
    priority = input("Enter priority (high/med/low): ")
    while priority != "high" and priority != "med" and priority != "low":
        print("Please enter priority as high, med, or low")
        priority = input("Enter priority (high/med/low): ")
    ToDo.append({
        "name": name,
        "priority": priority
    })
    print(f"\nAdded {name} with priority = {priority}.\n")
    Menu()


def DeleteTask():
    print("\n~DELETE TASK~\n")
    DelViewTask()
    choice, confirm = GetDelChoice()
    if confirm == "y":
        print(ToDo[choice]["name"] + " was deleted.")
        del ToDo[choice]
    elif confirm == "n":
        print(ToDo[choice]["name"] + " was not deleted.")
    Menu()
    

def GetDelChoice():
    choice = input("\nChoose a task index to delete, or q to cancel: ")
    try:
        choice = int(choice)
    except:
        while type(choice) != int:
            if choice.lower() == 'q':
                Menu()
            choice = input("\nPlease choose an index in the range 0 - " + str(len(ToDo)-1) + ": ")
            try:
                choice = int(choice)
            except:
                pass
    while choice < 0 or choice > (len(ToDo) -1):
        choice = int(input("Selected index not in range. Enter index to delete: "))
    confirm = input("\nDelete task " + ToDo[choice]["name"] + f" at index {choice}? (y/n): ")
    while confirm != 'y' and confirm != 'n':
        confirm = input("\nEnter (y/n): ")
    return choice, confirm

def DelViewTask():
    print("\n.......Task List......\n")
    index = 0
    for task in ToDo:
        print(f"{index} - " + ToDo[index]["name"] + " --- " + ToDo[index]["priority"])
        index +=1


def ViewTask():
    print("\n.......Task List......\n")
    index = 0
    for task in ToDo:
        print(f"{index} - " + ToDo[index]["name"] + " --- " + ToDo[index]["priority"])
        index +=1
    confirm = input("\nPress m to return to menu.\n")
    while confirm != 'm' and confirm != 'M':
        confirm = input("\nPress m to return to menu.\n")
    Menu()
    

Menu()
