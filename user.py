import pyperclip


class User:
    """
    Class that generates new instances of users

    Meant to be in the same indent with the function below
    """
    user_list = []

    def __init__(self, first_name, last_name, password):
        """
        __init__ method that helps us define for our objects.

        i.e
          Args:
              first_name: New user first name.
              last_name: New user last name.
              password: New user  password address.

        The "self" python keyword can be likened to "this" in java & javascript
        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
#
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method delete a saved user from the user_list.
        """
        User.user_list.remove(self)

    @classmethod
    def find_by_first_name(cls, first_name):

        for user in cls.user_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def user_exist(cls, first_name):
        for user in cls.user_list:
            if user.first_name == first_name:
                return True
        return False

    @classmethod
    def display_users(cls):
        return cls.user_list

    # @classmethod
    # def copy_password(cls, first_name):
    #     user_found = User.find_by_first_name(first_name)
    #     pyperclip.copy(user_found.password)
