#!/usr/bin/env python3.9
from credentials import Credentials
from users import Users


def create_user(username, password):
    """
    Function to create a new user
    """
    new_user = Users(username, password)
    return new_user


def save_user(users):
    """
    Function to save user
    """

    users.save_user()


def display_users():
    """
    function that returns all the saved users
    """
    return Users.display_users()


def login_verify(username, password):
    """
    function that checks whether a user exist then logs them to the credentials section
    """
    check_user = Credentials.login_user(username, password)
    return check_user


def create_credential(account, user_name, account_password):
    new_credential = Credentials(account, user_name, account_password)
    return new_credential


def save_credentials(credentials):
    credentials.save_credential()


def display_credentials():
    """
    Functions that displays all saved credentials
    """
    return Credentials.display_credentials()


def delete_credentials(credentials):
    """
    Function that deletes chosen credential
    """
    credentials.delete_credential()


def find_credential(account):
    """
    Functions to find credential by username and returns credential
    """
    return Credentials.find_by_account(account)


def check_existing_credentials(account):
    """
    Functions that checks if credential exists with specified username and returns a Boolean
    """
    return Credentials.credential_exists(account)


def generate_password(length):
    """
    generates a random password for the user
    """
    random_Password = Credentials.random_password()
    return random_Password


def main():
    print("Hello. Create your credentials account. But first, what is your name?")
    current_user = input().lower()

    print(f"Hello {current_user}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes: cc - create new credential, dc - display credentials, delc - delete credential, fc - find credential,, ex - exit account")
        short_code = input().lower()

        if short_code == 'cc':
            print("New Credential")
            print("-"*10)
            print("Account Name e.g Twitter, Instagram etc")
            account = input()

            print("Account username")
            user_name = input()

            while True:
                print(
                    "choose tp - To type your own password: \n gp - To generate a random password")
                choice_pwd == input().lower()
                if choice_pwd == 'tp':
                    print("Account password")
                    account_password = input()
                    break
                elif choice_pwd == 'gp':
                    account_password = generate_password(length)
                    break
                else:
                    print("invalid password please try again")

            save_credentials(create_credential(
                account, user_name, account_password))
            print('\n')
            print(
                f"New Credential {account} {user_name} {account_password} created")
            print('\n')

        elif short_code == 'dc':
            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credentials in display_credentials():
                    print(
                        f"{credentials.account} {credentials.user_name} {credentials.account_password}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'delc':
            print("Enter the account you want to delete")
            search_account = input()
            if check_existing_credentials(search_account):
                search_credential = find_credential(search_account)
                search_credential.delete_credential()
                print('\n')
                print(
                    f"Your account credentials for: {search_credential.account} successfully deleted.")
                print('\n')

        elif short_code == 'fc':
            print("Enter the account you want to search for")
            search_account = input()
            if check_existing_credentials(search_account):
                search_credential = find_credential(search_account)
                print(
                    f"{search_credential.account} {search_credential.user_name} {search_credential.account_password}")
                print("-" * 20)
            else:
                print("Credential does not exist")
        elif short_code == 'ex':
            print("See ya!")
            break
        else:
            print("I didn't catch that. Please use the short codes provided")


if __name__ == '__main__':
    main()
