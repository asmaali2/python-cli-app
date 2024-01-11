# contact_book/cli.py
# import click

from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from  models import Contact, Group, session

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

    # print(f"My name is: {name}")


input_contacts()
