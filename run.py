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
