# contact_book/cli.py
# import click

from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from  models import Contact, Group, session

def add_contact():
    """Add a new contact to the database."""
    name = input("Enter Name: ")
    email = input("Enter Email Address: ")
    phone = input("Enter Phone number: ")
    address= input("Enter Address: ")
    # Create instance of model class with user inputs as arguments
    
    new_contact = Contact(name=name, email=email, phone=phone,address=address)
    try:
        session.add(new_contact)
        session.commit()
        print(f"\nContact '{name}' added.\n")
        session.close()
    except Exception as e:
        print(f"\nError adding contact:\n{e}\n")

def show_contacts():
    """Show all contacts in the database."""
    results = session.query(Contact).order_by(Contact.name).all()
    if results:
        for contact in results:
            print(f"ID: {contact.id}, Name: {contact.name}")
    else:
        print("\nNo contacts found.")

def add_group():
    group_name = input("Enter Group Name: ")
    new_group = Group(name=group_name)
    session.add(new_group)
    session.commit()
    print(f'\nGroup "{group_name}" created.\n')

# ... (other imports)
def input_contacts():
    while True:
        print("Please select option")
        print('1: Add new contact')
        print('2: Show all contacts')
        print('3: Add group')
        print('4: Exit')

        choice= int(input("\nEnter option: "))
        if choice == 1:
            print("\nSelected add contact\n")
        elif choice==2:
            print("\nSelected show contacts\n")
        elif choice == 3:
            print("\nSelected Add group\n")
        elif choice == 4:
            exit()

def input_contacts():
    while True:
        print("\nPlease select option")
        print('1: Add new contact')
        print('2: Show all contacts')
        print('3: Add group')
        print('4: Exit')

        choice= input("\nEnter option: ")
        if choice == '1':
            add_contact()
        elif choice=='2':
            show_contacts()
        elif choice == '3':
            add_group()
        elif choice == '4':
            break


    # print(f"My name is: {name}")


input_contacts()
