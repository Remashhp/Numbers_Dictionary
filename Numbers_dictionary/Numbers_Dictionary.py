from NumberManager import HashList

number_manager = HashList()

while True:
        print("Available actions:")
        print("1. Add a number")
        print("2. Search for a name")
        print("3. Exit")

        choice = input("Select an action: ")

        if choice == '1':
            name = input("Enter the name of the owner of the number: ")
            number = input("Enter the number that you want to add: ")
            number_manager.add_number(name, number)
        elif choice == '2':
            name_to_search = input("Enter the name you want to search for: ")
            number_manager.search(name_to_search) 