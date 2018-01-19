#!/usr/bin/env python3.6
# print("Jedi")
from p_manager import Passwords


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
