import unittest
from users import Users


class TestUsers(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    '''

    def setUp(self):
        self.new_user = Users("Joy", "0000")

    def test_init(self):
        self.assertEqual(self.new_user.username, "Joy")
        self.assertEqual(self.new_user.password, "0000")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(Users.users_list), 1)

    def tearDown(self):
        """
        tearDown method to clean up after each test case has run

        """
        Users.users_list = []

    def test_save_mulitple_user(self):
        """
        test to see if we can save multiple contact objects

        """
        self.new_user.save_user()
        test_user = Users("Test", "1111")
        test_user.save_user()
        self.assertEqual(len(Users.users_list), 2)

    def test_delete_user(self):
        """
        test to see if we can remove a user from our user list
        """
        self.new_user.save_user()
        test_user = Users("Test", "1111")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(Users.users_list), 1)

    def test_find_user_by_username(self):
        """
        test to check if we can find a user by their username
        """
        self.new_user.save_user()
        test_user = Users("Test", "1111")
        test_user.save_user()
        found_user = Users.find_by_username("Test")

        self.assertEqual(found_user.password, test_user.password)

    def test_user_exists(self):
        """
        Check to see if user exists
        """
        self.new_user.save_user()
        test_user = Users("Test", "1111")
        test_user.save_user()

        user_exists = Users.user_exists("Test")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        """
        method to return all the lists of users saved
        """

        self.assertEqual(Users.display_users(), Users.users_list)


if __name__ == '__main__':
    unittest.main()
