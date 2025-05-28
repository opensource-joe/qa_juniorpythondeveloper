###############################################################################
# Python Unittest - Patching
###############################################################################
import getpass
import unittest
from unittest.mock import patch

import bcrypt

class UnknownUser(Exception):
    ''' Exception raised if a username is not found. '''

class UserManagement:
    ''' Fake user management system. '''

    def __init__(self):
        self.creds = {}

    def upsert_user(self, username, password):
        self.creds[username] = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def creds_for(self, username):
        try:
            return self.creds[username]
        except KeyError:
            raise UnknownUser(f'Authentication for {username} failed.')

    def authenticate(self):
        username = input('username: ')
        password = getpass.getpass('password: ').encode()
        passhash = self.creds_for(username)
        return bcrypt.checkpw(password, passhash)


class TestChallenge3(unittest.TestCase):

    def test_valid_users(self):
        accounts = [
            ('admin', 'secure!'),
            ('usera', 'secret!'),
            ('userb', 'stealth'),
            ('userc', 'hidden!'),
        ]
        user_management = UserManagement()
        ###############################################################################
        # 
        # Assignment:
        #
        # 
        # Test the UserManagement.authenticate method by patching the 
        # input and getpass callables.
        # 
        # 1.) For each username and password in accounts:
        #       a.) Call user_management.upsert_user.
        # 
        #       b.) Patch the built-in input and getpass.getpass callables to return the 
        #           username and password respectively.
        #       
        #       c.) Assert that calling user_management.authenticate returns True.
        #
        ###############################################################################
        # Add test code below
        
        # Test the UserManagement.authenticate method by patching the input and getpass callables.
        # For each username and password in accounts:
        for username, password in accounts:
            # a.) Call user_management.upsert_user.
            user_management.upsert_user(username, password)
            
            # b.) Patch the built-in input and getpass.getpass callables to return the username and password respectively.
            with patch('builtins.input', return_value=username), \
                 patch('getpass.getpass', return_value=password):
                
                # c.) Assert that calling user_management.authenticate returns True.
                self.assertTrue(user_management.authenticate())
        
        # End test code
        ###############################################################################
        

    
    def test_invalid_users(self):
        accounts = [
            ('a', 'a'),
            ('b', 'b'),
        ]
        user_management = UserManagement()
        ###############################################################################
        # 
        # Assignment:
        #
        # 
        # Ensure that UserManagement.authenticate raises an UnknownUser exception if
        # a username is not found.
        # 
        # 1.) For each username and password in accounts:
        #       a.) Patch the built-in input and getpass.getpass callables to return the 
        #           username and password respectively.
        #       
        #       b.) Assert that calling user_management.authenticate raises 
        #           an UnknownUser exception
        #
        #
        # NOTE: The primary difference between this and the previous test is that this
        #       test doesn't call the upsert_user method. 
        #
        ###############################################################################
        ###############################################################################
        # Add test code below
        
        # Ensure that UserManagement.authenticate raises an UnknownUser exception if a username is not found.
        # For each username and password in accounts:
        for username, password in accounts:
            # a.) Patch the built-in input and getpass.getpass callables to return the username and password respectively.
            with patch('builtins.input', return_value=username), \
                 patch('getpass.getpass', return_value=password):
                
                # b.) Assert that calling user_management.authenticate raises an UnknownUser exception
                with self.assertRaises(UnknownUser):
                    user_management.authenticate()
        
        # End test code
        ###############################################################################

if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))
