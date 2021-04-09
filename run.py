#!/usr/bin/env python3.9
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


def delete_user(users):
    """
    function to delete users
    """
    users.delete_user()


def find_user(user):
    """
    function that finds user by username
    """
    user.find_user(username)


def check_existing_user(username):
    """
    function to find existing user and returns a Boolean
    """
    return Users.user_exists(username)


def display_users():
    """
    function that returns all the saved users
    """
    return Users.display_users()


def main():
    print("Hello. Welcome to you password manager.What is your Name?")
    current_user = input()
    print(f"Hello {current_user}.what would you like to do?")
    print('/n')

    while True:
        print("User these short codes : cu - create user, delu - delete user, du - display users, fu - find user, ex - exit users")
        short_code = input().lower()

        if short_code == 'cu':
            print("Create an Account")
            print("-"*17)

            print("Enter a Username")
            username = input()

            print("Enter a password")
            password = input()

            save_user(create_user(username, password))
            print('/n')
            print(f"New User {username} {password} created")
            print('/n')

        elif short_code == 'delu':
            print("insert username you want to delete")
            username = input()
            if check_existing_user(username):
                delete_user(find_user(username))
                print("{username} account has been deleted")

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all the users")
                print('/n')

                for users in display_users():
                    print(f"{users.username} {users.password}")
                print('/n')

            else:
                print('/n')
                print("You dont seem to have any users saved yet")
                print('/n')

        elif short_code == 'fu':
            print("Enter the username you want to search for")

            search_username = input()
            if check_existing_user(search_username):
                search_user = find_user(search_username)
                print(f"{search_user.username}")
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
