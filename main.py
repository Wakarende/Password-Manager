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


def find_by_username(username):
    """
    function that finds user by username
    """
    return Users.find_by_username(username)


def check_existing_user(username):
    """
    function to find existing user and returns a Boolean
    """
    return Users.user_exists(username)


def login_verify(username, password):
    """
    function that checks whether a user exist then logs them to the credentials section
    """
    check_user = Credentials.login_user(username, password)
    return check_user


def create_credential(account, user_name, account_password):
    """
    Function to create new credential
    """
    new_credential = Credentials(account, user_name, account_password)
    return new_credential


def save_credentials(credentials):
    """
    Function to save all users
    """
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
    print("Hello. Create your password account. But first, what is your name?")
    current_user = input()
    print(f"Hello {current_user}. What would you like to do?")
    print('\n')
    while True:
        print("Choose from the following short codes: cu - create user-account, du - display user accounts, delu - deletes user-account, fu - finds user by username li - login into account, en - end")
        short_code = input("Input you choice: ")
        if short_code == 'cu':
            print("Account Username: ")
            print("-"*20)
            username = input()
            print("Enter account password")
            print("-"*20)
            password = input()
            if len(password) >= 4:
                save_user(create_user(username, password))
                print('\n')
                print(f"New User created")
                print("-"*20)
                print(f"User: {username}")
                print(f"Password: {password}")
                print('\n')

            else:
                print(
                    "Your password is too short.Please create a password 4 characters or more.")

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all the users")
                print('\n')

                for users in display_users():
                    print("-"*20)
                    print(f"Username:{users.username}")
                    print(f"Password:{users.password}")
                    print("-"*20)
                print('\n')

            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')

        elif short_code == 'fu':
            print("Enter the username you want to search for")

            search_username = input()
            if check_existing_user(search_username):
                search_user = find_by_username(search_username)
                print("-"*20)
                print(f"User: {search_user.username}")
                print(f"Password: {search_user.password}")
                print('-'*20)

            else:
                print("That user does not exist")

        elif short_code == 'li':
            print("Enter your Account Username and Password to log in :")
            print("-"*20)
            username = input("Username: ")
            password = input("Password: ")
            print("-"*20)

            if check_existing_user(username):
                print(
                    f"Hello {username}. Welcome to your account.Choose and option to continue.")
                print('\n')
            else:
                print("Invalid username. Please input a valid username")
                break
            while True:
                print("Use these short codes: cc - create new credential,dc - display credentials, delc - delete credential, fc - find credential, ex - exit account")
                short_code = input().lower()

                if short_code == 'cc':
                    print("New Credential")
                    print("-"*20)
                    print("Account Name e.g Twitter, Instagram etc")
                    print("-"*20)
                    account = input()

                    print("Account username")
                    print("-"*20)
                    user_name = input()

                    while True:
                        print(
                            "choose tp - To type your own password: \n gp - To generate a random password")
                        choice_pwd = input().lower()
                        if choice_pwd == 'tp':
                            print("Account password")
                            print("-"*20)
                            account_password = input()
                            save_credentials(create_credential(
                                account, user_name, account_password))
                            print('\n')
                            print(f"New Credential:")
                            print("-"*20)
                            print(f"Account: {account} ")
                            print('\n')
                            print(f"Username: {user_name}")
                            print('\n')
                            print(f"Password: {account_password}")
                            print("-"*20)
                            print('\n')
                            break
                        elif choice_pwd == 'gp':
                            account_password = generate_password(length=8)
                            print(f"New password is {account_password}")
                            save_credentials(create_credential(
                                account, user_name, account_password))
                            print(f"New Credential:")
                            print("-"*20)
                            print(f"Account: {account} ")
                            print(f"Username: {user_name}")
                            print(f"Password: {account_password}")
                            print("-"*20)
                            print('\n')
                            break
                        else:
                            print("You did not create a password. Please try again.")
                            break
                elif short_code == 'dc':
                    if display_credentials():
                        print("Here is a list of all your credentials")
                        print('\n')

                        for credentials in display_credentials():
                            print("Here are all your credentials.")
                            print("-"*20)
                            print(f"Account: {credentials.account}")
                            print(f"Username: {credentials.user_name}")
                            print(f"Password: {credentials.account_password}")
                            print("-"*20)
                            print('\n')
                            break
                        else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')
                elif short_code == 'delc':
                    print(
                        "Enter the credential-account you want to delete e.g Twitter, Instagram etc.")
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

        elif short_code == 'delu':
            print("insert username you want to delete")
            search_username = input()
            if check_existing_user(search_username):
                remove_user = find_by_username(search_username)
                remove_user.delete_user()

                print(f"{remove_user.username} account has been deleted")

        elif short_code == 'en':
            print(f"Bye!")
            break

        else:
            print("Please use the short codes provided to navigate.")


if __name__ == '__main__':
    main()
