class Credentials:

    credential_list = []

    def __init__(self, account, user_name, account_password):
        """
        Method for credentials to be stored
        """
        self.account = account
        self.user_name = user_name
        self.account_password = account_password
