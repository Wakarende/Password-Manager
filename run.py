#!/usr/bin/env python3.9
from users import Users
from credentials import Credentials


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


def delete_user(users):
    """
    function to delete users
    """
    users.delete_user()


def find_by_username(users):
    """
    function that finds user by username
    """
    users.find_by_username(username)


def check_existing_user(username):
    """
    function to find existing user and returns a Boolean
    """
    return Users.user_exists(username)


def create_credential(account, user_name, account_password):
    new_credential = Credentials(account, user_name, account_password)
    return new_credential


def save_credentials(credentials):
    credentials.save_credential()


def display_all_credentials():
    """
    Functions that displays all saved credentials
    """
    return Credentials.display_all_credentials()


def delete_credentials(credentials):
    """
    Function that deletes chosen credential
    """
    credentials.delete_credential()


def find_credential(user_name):
    """
    Functions to find credential by username and returns credential
    """
    return Credentials.find_by_credential_username(user_name)


def check_existing_credentials(user_name):
    """
    Functions that checks if credential exists with specified username and returns a Boolean
    """
    return Credentials.credential_exists(user_name)


def main():
    print("Hello. Welcome to you password manager.What is your Name?")
    current_user = input()

    print(f"Hello {current_user}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create user, delu - delete user, du - display users, fu - find user, ex - exit users")
        short_code = input().lower()

        if short_code == 'cu':
            print("Create an Account")
            print("-"*17)

            print("Enter a Username")
            username = input()

            print("Enter a password")
            password = input()

            save_user(create_user(username, password))
            print('\n')
            print(f"New User {username} {password} created")
            print('\n')

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all the users")
                print('\n')

                for users in display_users():
                    print(f"{users.username} {users.password}")
                print('\n')

            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')
        elif short_code == 'delu':
            print("insert username you want to delete")
            search_username = input()
            if check_existing_user(search_username):
                remove_user = find_by_username(search_username)
                remove_user.delete_user()

                print(f"{remove_user.username} account has been deleted")

        elif short_code == 'fu':
            print("Enter the username you want to search for")

            search_username = input().lower()
            if check_existing_user(search_username):
                search_user = find_by_username(search_username)
                print(f"User: {search_user.username}")
                print(f"Password: {search_user.password}")
                print('-'*20)

            else:
                print("That user does not exist")

        elif short_code == "ex":
            print("Bye Bye!")
            break
        else:
            print("Please use the short codes above")


if __name__ == '__main__':
    main()
