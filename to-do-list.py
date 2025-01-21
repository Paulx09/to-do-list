runInitial = True
tasks_list = []

# Función para mostrar la lista de tareas
def showTasks():
    global tasks_list
    print("\n****** Your Tasks ******")
    for item in tasks_list:
        print(f"{tasks_list.index(item) + 1}. {item}")
    print("****** Your Tasks ******\n")

# Función de opciones del menu
def showOptions():
    print("\nSELECT AN OPTION: ")
    print("1. Create a new task")
    print("2. Mark your tasks")
    print("3. Delete a task")
    print("4. Exit")

#Función para crear las tareas
def createTask():
    global tasks_list
    print("\n*** Create a new task ***")
    task = input("Enter your new task: ")
    tasks_list.append(task)
    showTasks()

# Función principal del programa
def main():
    global runInitial
    print(".: WELCOME TO A TO DO LIST IN PYTHON :.")
    while runInitial:
        showOptions()
        option = int(input("\nEnter your number option: "))
        
        match option:
            case 1: 
                createTask()
            case 2:
                print("MARK A TASK: ")
            case 3:
                print("DELETE A TASK: ")
            case 4:
                print("LEAVING THE PROGRAM...")
            case _:
                print("Invalid option. Try again...")

if __name__ == "__main__":
    main()