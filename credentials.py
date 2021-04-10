import string
import random


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

    @classmethod
    def verify_user(cls, username, password):
        """
        Method to check if user is on the user list
        """
        login_user = ""
        for user in Users.users_list:
            if(user.username == username and user.password == password):
                login_user == user.username
        return login_user

    def random_password(length=8):
        """
        Method to generate random password
        """
        password = string.ascii_letters
        result_str = ''.join(random.choice(password)for i in range(8))
        return result_str
