class Users:
    """
    Class that generates new instances of contacts.
    """
    users_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into user_list

        """
        Users.users_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes save user from the user_list
        """
        Users.users_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        """
        Method that takes in a username and returns the account that matches the username

        Args:
        Username: name used to create account

        Returns:
        user
        """

        for user in Users.users_list:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls, username):
        """
        Method to check if user exists on user list
        Returns: Boolean depending if user exists
        """
        for user in Users.users_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def display_users(cls):
        """
        method that returns the user list
        """
        return cls.users_list
