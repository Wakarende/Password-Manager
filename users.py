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
        save_user method saves user objects into contact_list

        """
        Users.users_list.append(self)
