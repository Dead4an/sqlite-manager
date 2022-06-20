# Standart modules
from cmath import e
from multiprocessing import connection
import os
from sqlite3 import connect

# Other modules
from database_manager.manager import Manager
from database_manager.user import User

# Main menu
MAIN_MENU = (
"""
1. Create a new user table
2. Display users
3. Add a user to the user table
4. Delete a user from the user table
5. Get a user by id
6. Truncate the user table
0. Exit
// """
)

# Main program funcion
def main():
    try:
        # Set connetion
        connection = Manager()
        connection.create_connetion()

        while True:
            chosen_option = choose_menu_option()

            if chosen_option != 0:
                commit_operation(connection, chosen_option)
                continue

            flag = input('\n[?] Close the program? (Y/N): ').lower()
            if flag == 'y':
                print('\n[!] Closing the program...')
                break

    except Exception as _ex:
        print(f'\n[!] Exception: {_ex}')

    finally:
        connection.close_connetion()
        input('\n[!] Press Enter to exit')

# Functions
def choose_menu_option():
    """ Returns a chosen option """

    chosen_option = None
    allowed_values = (range(7))

    while chosen_option not in allowed_values:
        try:
            chosen_option = int(input(MAIN_MENU))

            if chosen_option not in allowed_values:
                print("\n[!] There's not this option")

        except Exception as _ex:
            print(f'\n[!] Exception: {_ex}')

    return chosen_option


def commit_operation(connection: Manager, chosen_option: int):
    """ Commits a chosen operatino to the database """

    match chosen_option:
        case 1: 
            connection.create_user_table()

        case 2:
            users = connection.get_users()
            print('\n' + ('=' * 40))
            for user in users:
                print(f"ID: {user[0]} | Name: {user[1]} | Password: {user[2]}")
            print('=' * 40)

        case 3: 
            __name = input('Input name: ')
            __password = input('Input password: ')
            connection.add_user(User(__name, __password))

        case 4:
            connection.delete_user()

        case 5:
            user = connection.get_user()
            print(user)
            print(f'\nID: {user[0]} | Name: {user[1]} | Password: {user[2]}')

        case 6:
            flag = input('\n[?] Are you sure you want to truncate the user table? (Y/N): ').lower()
            if flag == 'y':
                connection.truncate_user_table()

# Program enter point
if __name__ == '__main__':
    main()
