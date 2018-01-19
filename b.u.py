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


def find_profie(account_name):
    """
    Function finds password by account name and returns full details
    """
    return Passwords.find_by_account(account_name)


def display_profiles():
    """
    Function returns all the save profiles
    """
    return Passwords.display_profiles()
