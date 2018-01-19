#!/usr/bin/env python3.6
# print("Jedi")
from locker import Passwords
from user import User

"""
Users Details
"""


def create_user(fname, lname, phone, email):
    """
    Function to create a new user_list
    """
    new_user = User(fname, lname, phone, email)
    return new_user

# Save users


def save_users(user):
    """
    Function to save user
    """
    user.save_user()


# Delete user


def del_user(user):
    """
    Function to delete a user
    """
    user.delete_user()


# Finding a user


def find_user(number):
    """
    Function that finds a user by number and returns the contract
    """
    return User.find_by_number(number)

# Check if a contract exists


def check_existing_user(number):
    """
    Function that checks if a user exists with that number and return Boolean
    """
    return User.user_exist(number)

# Displaying all users


def display_users():
    """
    Function that returns all the save users
    """
    return User.display_users()

# Copy pasting


def copy_email(number):
    """
    Function that copys to machines clipboard
    """
    return User.copy_email()


"""
Accounts and Passwords
"""


def create_profile(account_name, account_password, password_length):
    """
    Function to create new_profile
    """
    new_profile = Passwords(account_name, account_password, password_length)
    return new_profile


def save_profile(profile):
    """
    Function to save profile
    """
    profile.save_profile()


def find_profile(account_name):
    """
    Function finds password by account name and returns full details
    """
    return Passwords.find_by_account(account_name)


def profile_exists(account_name):
    """
    Function that check if a profile exists using an account name to return a
    boolean if it is found or not.
    """
    return Passwords.profile_exists()


def display_profiles():
    """
    Function that returns all save profiles
    """
    return Passwords.display_profiles


def copy_password(account_name):
    """
    Function that allows us to copy a password from matching account_name
    """
    return Passwords.copy_password()


def main():
    print("Hello! Welcome to your password manager. What is your name?")
    user_name = input()
    print("")

    print(f"Hi {user_name}. What would you like to do?")
    print("")

    while True:
        print("""Use these short codes:
              cn - create new account
              np - create password profile,
              dp- display password locker profiles,
              fp - find a password profile,
              ex - exit contact list.""")
        short_code = input().lower()
        print("_" * 20)
        if short_code == "nc":
            print("New Contact")
            print("_" * 100)
        elif short_code == "ex":
            print("")
            print(
                "*" * 10 + " Thank you for visiting password locker. Come again! Bye :) " + "*" * 10)
            print("")
            break


if __name__ == '__main__':
    main()
