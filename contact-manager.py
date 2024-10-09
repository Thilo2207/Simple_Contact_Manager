import json

filename = "contact.json"

def contacts_load():
    try:
       with open(filename,"r") as file:
           return json.load(file)
    except:
        return {}

def save_contacts():
    with open(filename,"w") as file:
        json.dump(contact_manager, file, indent = 4)

def search_contacts(specific_name):
    found_contacts = {name:details for name,details in contact_manager.items() if specific_name.lower() in name.lower()}
    if found_contacts:
        for  name,details in found_contacts.items():
            print(f"{name} : {details}")
    else:
        print(f"Contact '{name}' Not Found")

def update_contacts(name,phone = None,email = None):
    if name in contact_manager:
        if phone:
            contact_manager[name]["Phone"] = phone
        if email:
            contact_manager[name]["Email ID"] = email
        if phone and email:
            contact_manager[name] = {"Phone":phone,"Email Id":email}
        save_contacts()
        print(f"Contact '{name}' updated successfully")
    else:
        print(f"Contact '{name}' Not Found")

def add_contacts(name,phone,email):
    if name in contact_manager:
        print(f"Contact '{name}' already exists")
    else:
        contact_manager[name] = {"Phone":phone,"Email ID": email}
        save_contacts()
        print(f"Contact '{name}' added successfully.")

def delete_contacts(name):
    if name in contact_manager:
        del contact_manager[name]
        save_contacts()
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' Not Found")

def list_contacts():
    if contact_manager:
        for name in sorted(contact_manager):
            print(f"{name} : {contact_manager[name]}")
    else:
        print("No Contacts Available")

contact_manager = contacts_load()

def menu():
     while True:
        print("\nContact Manager")
        print("1. Add New Contact")
        print("2. Search Contact (Partial Search Supported)")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter Name: ")
            phone = int(input("Enter Phone Number: "))
            email = input("Enter Email Id: ")
            add_contacts(name,phone,email)

        elif choice == "2":
            name = input("Enter Which name want you search: ")
            search_contacts(name)
        
        elif choice == "3":
            name = input("Enter name which deatails do you want change: ")
            choice = input("Enter what change - 'phone','email' or 'both': ")

            if choice == 'phone':
                phone = int(input("Enter the Phone Number: "))
                update_contacts(name,phone,email=None)
            elif choice == 'email':
                email = input("Enter Email Id: ")  
                update_contacts(name,phone=None,email=email)
            elif choice == 'both':
                phone = int(input("Enter the Phone Number: "))
                email = input("Enter Email Id: ")
                update_contacts(name,phone,email)
        
        elif choice == "4":
            name = input("Enter which contact do want delete: ")
            delete_contacts(name)
        
        elif choice == "5":
            list_contacts()
        
        elif choice == "6":
            print("Exiting Contact Manager")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

menu()
