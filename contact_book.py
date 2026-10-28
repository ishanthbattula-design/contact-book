contacts = {}

while True:
    print("\n---Contact book---")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ").strip()
    print(f"You chose option '{choice}'") 
    
    if choice == "1":
        new_name = input("Enter contact name: ").strip()
        phone = input("Enter contact's phone number: ").strip()
        contacts[new_name] = phone
        print(f"Contact {new_name} added successfully.")
        
    elif choice == "2":
        if contacts:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Contact book is empty.")
            
    elif choice == "3":
        search_name = input("Enter a contact name to search: ").strip()
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print(f"Contact '{search_name}' not found.")
            
    elif choice == "4":
        delete_name = input("Enter a contact name to delete: ").strip()
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"Contact '{delete_name}' deleted successfully.")
        else:
            print(f"Contact '{delete_name}' not found.")
            
    elif choice == "5":
        print("Exiting the contact book. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
