class Users:
    """
    Class that generates new instances of users.
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

        for users in cls.users_list:
            if users.username == username:
                return users

    @classmethod
    def user_exists(cls, username):
        """
        Method to check if user exists on user list
        Returns: Boolean depending if user exists
        """
        for users in cls.users_list:
            if users.username == username:
                return True
        return False

    @classmethod
    def display_users(cls):
        """
        method that returns the user list
        """
        return cls.users_list
