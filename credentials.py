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
    def find_by_account(cls, account):
        """
        Method that takes in a username and returns a credential that matches the username
        """
        for credential in cls.credential_list:
            if credential.account == account:
                return credential

    @classmethod
    def credential_exists(cls, account):
        """
        Method to check if credential exists in credential list
        """

        for credential in cls.credential_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method that returns the credentials list
        """
        return cls.credential_list
