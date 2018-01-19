#!/usr/bin/env python3.6
import pyperclip
"""
1.Generate password
2.Save password
3.Tear Down
4.Save multiple
5.Delete password profile
6.Display
7.Find by profile
8.Copy_paste
"""
# import random

""""
We'll start by defining the class that we will help build the password manager.
So in for our application we will need only:
1. Accounts - different accounts that need a password
2. Passwords - generated or client defined passwords.
"""


class User:
    def __init__(self, first_name, last_name, profile_key):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_key = profile_key


class Passwords:
    """
    Class that generates new instances of contacts.
    Below we create our class variable. An empty password_list[]
    It stores our passwords and account info as a list.
    """
    password_list = []

    def __init__(self, account_name, account_password, password_length):
        """
        The init method allows us to create new instances of our class.
        It also allows us to pass in properties for the object.

        Note that methods are a bit different from function in one way.
        They always have "self" added to the beginning of their parameter list.


        So our object will have an account name and password
        """

        self.account_name = account_name
        self.account_password = account_password
        self.password_length = password_length

    def save_profile(self):
        """
        Here we build our save profile function that will append every account
        and password profile.
        When we import it and use it on our test_save profile test-case...it
        should work.
        """
        Passwords.password_list.append(self)

    """
    Below we encounter decorators in python.
    They basically allow us to make simple modifications to callable objects
    like functions, methods, or classes

    Here we want to allow some of our functions to apply to the entire class.
    """

    @classmethod
    def profile_exists(cls, account_name):
        """
        Method checks if a profile exists from password_list. It takes in the
        name and returns a boolean if it finds a matching account.
        """
        for profile in cls.password_list:
            if profile.account_name == account_name:
                return True
        return False

    @classmethod
    def display_profiles(cls):
        """
        Method that will return profile list.
        """
        return cls.password_list

    @classmethod
    def find_by_account(cls, account_name):
        """
        This method takes in an account name and returns the password matching
        the account.
        """
        for profile in cls.password_list:
            if profile.account_name == account_name:
                return profile

    @classmethod
    def copy_password(cls, account_name):
        password_found = Passwords.find_by_account(account_name)
        pyperclip.copy(password_found.account_password)

# print("How long do you want your password:")
# password_length = int(input())
# string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+{}\|"';>./,`!@#$^&*()`'
# password = "".join(random.sample(string, password_length))
# print(password)
