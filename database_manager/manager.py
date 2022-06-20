# Standart modules
import os
import sqlite3
from sqlite3 import Error

# Other modules
from .user import User

# Queris
CREATE_USER_TABLE_QUERY = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR(20), password VARCHAR(20));'
SELECT_ALL_USERS = 'SELECT * FROM users'
SELECT_USER_BY_ID = 'SELECT * FROM users WHERE id='
DELETE_USER_FROM_TABLE = 'DELETE FROM users WHERE id='
TRUNCATE_USER_TABLE = 'DELETE FROM users'

# Paths
BASE_DIR = os.getcwd()

# Manager class
class Manager:
    """ Database manager """

    def __init__(self, database_path=None):
        """ Inits a manager """

        self._database_path = database_path

        if not self._database_path:
            database_path = input('Input database name: ')
            self._database_path = database_path

        self._connetion = None
        self._cursor = None


    def create_connetion(self):
        """ Creates connetion with a database """

        try:
            self._connetion = sqlite3.Connection(self._database_path)
            self._cursor = self._connetion.cursor()
            print('\n[!] Connection created successfully')

        except Error as _ex:
            print(f'\n[!] Exception: {_ex}')


    def close_connetion(self):
        """ Closes connetion """

        try:
            self._cursor.close()
            self._connetion.close()

        except Exception or Error as _ex:
            print(f'\n[!] Exception: {_ex}')

    
    def create_user_table(self):
        """ Creates a user table """

        try:
            self._cursor.execute(CREATE_USER_TABLE_QUERY)
            self._connetion.commit()
            print('\n[!] User table created successfully')

        except Error as _ex:
            print(f'[!] Exception: {_ex}')

    
    def get_users(self):
        """ Return all users from the user table """

        try:
            self._cursor.execute(SELECT_ALL_USERS)
            users = self._cursor.fetchall()
            return users

        except Error as _ex:
            print(f'\n[!] Exception: {_ex}')


    def add_user(self, user: User):
        """ Adds a user to the table """

        try:
            __name = user.get_name()
            __password = user.get_password()

            self._cursor.execute(f'INSERT OR IGNORE INTO users (name, password) VALUES ("{__name}", "{__password}")')
            self._connetion.commit()

            print('\n[!] User added successfully')

        except Exception or Error as _ex:
            print(f'\n[!] Exception: {_ex}')


    def delete_user(self):
        """ Deletes a user from the user table """

        try:
            user_id = input('\n[!] Input the user id: ')
            user = self.get_user(user_id)
            flag = input(f'Are you sure you want to delete this user?\n\
                    ID: {user[0]} | Name: {user[1]}, | Password: {user[2]}\n(Y/N): ').lower()

            if flag == 'y':
                self._cursor.execute(f'{DELETE_USER_FROM_TABLE}{user_id}')
                self._connetion.commit()

        except Error as _ex:
            print(f'Exception: {_ex}')


    def get_user(self, user_id=None):

        try:
            if not user_id:
                user_id = input('\n[!] Input the user id: ')

            return self._cursor.execute(f'{SELECT_USER_BY_ID}{user_id}').fetchall()[0]   

        except Error as _ex:
            print(f'[!] Exception: {_ex}')

    
    def truncate_user_table(self):
        """ Truncates the user table """

        try:
            self._cursor.execute(TRUNCATE_USER_TABLE)
            self._connetion.commit()
            print('\n[!] Table truncated successfully')

        except Error as _ex:
            print(f'\n[!] Exception: {_ex}\n')
