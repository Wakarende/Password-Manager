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

    @classmethod
    def find_by_credential_username(cls, user_name):
        """
        Method that takes in a username and returns a credential that matches the username
        """
        for credential in Credentials.credential_list:
            if credential.user_name == user_name:
                return credential

    @classmethod
    def credential_exists(cls, user_name):
        """
        Method to check if credential exists in credential list
        """

        for credential in Credentials.credential_list:
            if credential.user_name == user_name:
                return True
        return False
