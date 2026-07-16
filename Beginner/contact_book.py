contacts = {}

while True:
    print("\n1. Add  2. Search  3. Delete  4. View  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter the name: ")
        contacts[name] = input("Enter the number: ")

    elif choice == "2":
        search = input("Enter the name to search: ")
        if search in contacts:
            print(contacts[search])
        else:
            print("Not found")

    elif choice == "3":
        dlt = input("Enter the name to delete: ")
        if dlt in contacts:
            del contacts[dlt]
            print("Removed")
        else:
            print("Not found")

    elif choice == "4":
        if not contacts:
            print("No contacts")
        else:
            for name, number in contacts.items():
                print(name, ":", number)

    elif choice == "5":
        print("Goodbye")
        break
