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


if __name__ == '__main__':
    unittest.main()
