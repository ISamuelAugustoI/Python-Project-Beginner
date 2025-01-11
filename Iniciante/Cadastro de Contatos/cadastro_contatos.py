"""
Author: Samuel Augusto
Date: 23/12/2024
Description: Código que simula um cadastro de contatos
"""
contacts = {}
def add_contact():
    name = str(input('Enter your name: '))
    phone = int(input('Enter your phone: '))
    email = str(input('Enter your email: '))
    notes = str(input('Enter your notes: '))
    if(name in contacts):
        print(f'This contact already exists.')
    else:
        contacts[name] = {'Phone': phone,'Email': email,'Notes': notes}
        print(f'Contact {name} added succesfully!')
def view_contacts():
    if(not contacts):
        print(f'No have contacts...')
    else:
        for i,j in contacts.items():
            print(f"Name: {i}")
            print(f"  Phone: {j['Phone']}")
            print(f"  Email: {j['Email']}")
            print(f"  Notes: {j['Notes']}")
def edit_contact():
    name = str(input('Enter the name of the contact: '))
    if(name in contacts):
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Notes: {contacts[name]['Notes']}")
        contacts[name]['Phone'] = phone = input("Enter new phone number: ")
        contacts[name]['Email'] = email = input("Enter new email: ")
        contacts[name]['Notes'] = notes = input("Enter new notes: ")
        print(f"Contact for {name} updated successfully!")
    else:
        print(f'contact not found...')
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if(name in contacts):
        del contacts[name]
        print(f"Contact for {name} deleted!")
    else:
        print("Contact not found!")
def search_contact():
    query = input("Enter the name to search: ")
    results = {name: details for name, details in contacts.items() if query.lower() in name.lower()}
    if results:
        print("\nSearch Results:")
        for i,j in results.items():
            print(f"Name: {i}")
            print(f"Phone: {j['Phone']}")
            print(f"Email: {j['Email']}")
            print(f"Notes: {j['Notes']}")
    else:
        print("No contacts found with that name!")
while True:
    print(f'===============================')
    print(f'Welcome to the Contact Manager:')
    print("[1] Add Contact")
    print("[2] View Contacts")
    print("[3] Edit Contact")
    print("[4] Delete Contact")
    print("[5] Search Contact")
    print("[6] Exit")
    choice = int(input('Enter your option: '))
    if(choice==1):
        print(f'--------------------')
        add_contact()
        print(f'--------------------')
    elif(choice==2):
        print(f'--------------------')
        view_contacts()
        print(f'--------------------')
    elif(choice==3):
        print(f'--------------------')
        edit_contact()
        print(f'--------------------')
    elif(choice==4):
        print(f'--------------------')
        delete_contact()
        print(f'--------------------')
    elif(choice==5):
        print(f'--------------------')
        search_contact()
        print(f'--------------------')
    elif(choice==6):
        print("Goodbye! See your later.")
        break
    else:
        print("Invalid choice. Please try again!")
