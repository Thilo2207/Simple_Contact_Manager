contact_manager = {
        "Thilo D Luffy":{"Phone":9369809589,"Email Id": "thilothama@gmail.com"},
        "Monkey D Luffy":{"Phone":9128476583,"Email Id":"luffyonepiece@gmail.com"},
        "Zoro":{"Phone":7485290110,"Email Id":"swoardsman@gmail.com"},
        "Robin":{"Phone":8876839201,"Email Id":"devilgirl@gmail.com"},
        "Chopper":{"Phone":9283049281,"Email Id":"doctor@gmail.com"}
    }

def contact_manager_func():
    
    sort_contact = sorted(contact_manager)
    alphabetical_order = {i:contact_manager[i] for i in sort_contact}

    return alphabetical_order

def edit_contacts():

    user = input("Enter what do you need - 'view' 'search','add','remove' or 'update': ")

    if user == 'view':
        return contact_manager_func()
    
    elif user == 'search':
        search = input("Enter contact Name which contact details you need: ")
        return f"{search} : {contact_manager[search]}"
    
    elif user == 'add':
        add_contact = input("Enter new contact name: ")
        number = int(input("Enter new contact number: "))
        email = input("Enter new contact Email Id: ")
        contact_manager[add_contact] = {"Phone":number,"Email ID":email}
        return contact_manager_func()
    
    elif user == 'remove':
        remove_contact = input("Enter which contact do you want delete: ")
        contact_manager.pop(remove_contact,"Not available contact")
        return contact_manager_func()
    
    elif user == 'update':
        edit = input("Which contact if you need update: ")
        phone_email = input("Enter 'phone' or 'email': ")
        if phone_email == 'Phone':
            phone = int(input("Enter Phone No: "))
            contact_manager[edit]["phone"] = [phone]
            return contact_manager_func()
        elif phone_email == 'email':
            email_id = input("Enter Email: ")
            contact_manager[edit]["Email Id"] = [email_id]
            return contact_manager_func()
        
    else:
        return "Please Enter Invalid Input"


result = edit_contacts()
print(result)

