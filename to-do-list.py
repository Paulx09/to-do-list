# Función de opciones del menu
def showOptions():
    print("\nSELECT AN OPTION:\n")
    print("1. Create a new task")
    print("2. Mark your tasks")
    print("3. Delete a task")
    print("4. Exit")

# Función principal del programa
def main():
    print(".: WELCOME TO A TO DO LIST IN PYTHON :.")
    while True:
        option = int(input("Enter your number option: "))
        match option:
            case 1: 
                print("CREATE A NEW TASK: ")
            case 2:
                print("MARK A TASK: ")
            case 3:
                print("DELETE A TASK: ")
            case 4:
                print("LEAVING THE PROGRAM...")
            case _:
                print("Invalid option")

if __name__ == "__main__":
    main()