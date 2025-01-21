import os

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
    os.system("cls")
    global tasks_list
    print("\n*** Create a new task ***")
    task = input("Enter your new task: ")
    tasks_list.append(task)
    showTasks()

# Función para marcar las tareas
def markTask():
    global tasks_list
    if tasks_list != []:
        os.system("cls")
        print("\n*** Mark your task ***")
        tasks_list_id = int(input("Enter the task number as completed: "))
        if tasks_list_id > len(tasks_list):
            print("Invalid task number. Try again...")
        else:
            tasks_list[tasks_list_id - 1] = tasks_list[tasks_list_id - 1] + " ✔"
            showTasks()
    else:
        print("There are no tasks to mark.")

# Función para eliminar las tareas
def deleteTask():
    global tasks_list
    if tasks_list != []:
        os.system("cls")
        print("\n*** Delete a task ***")
        tasks_list_id = int(input("Enter the task number to delete: "))
        if tasks_list_id > len(tasks_list):
            print("Invalid task number. Try again...")
        else:
            del tasks_list[tasks_list_id - 1]
            showTasks()
    else: 
        print("There are no tasks to delete.")

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
                markTask()
            case 3:
                deleteTask()
            case 4:
                print("LEAVING THE PROGRAM...")
                runInitial = False
            case _:
                print("Invalid option. Try again...")

if __name__ == "__main__":
    main()