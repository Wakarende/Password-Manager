class Credentials:

    credential_list = []

    def __init__(self, account, user_name, account_password):
        """
        Method for credentials to be stored
        """
        self.account = account
        self.user_name = user_name
        self.account_password = account_password

    def save_credential(self):
        """
        method that saves contact object
        """
        Credentials.credential_list.append(self)

    def delete_credential(self):
        """
        method deletes a saved credential from credential_list
        """
        Credentials.credential_list.remove(self)
