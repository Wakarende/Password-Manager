import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """
    Test class to test credentials class behaiours
    """

    def setUp(self):
        """
        Set up method that will run before each test case
        """
        self.new_credential = Credentials("Twitter", "Kare", "0")

    def test_init(self):
        """
        test if the objects have initialized properly
        """
        self.assertEqual(self.new_credential.account, "Twitter")
        self.assertEqual(self.new_credential.user_name, "Kare")
        self.assertEqual(self.new_credential.account_password, "0")

    def test_save_credential(self):
        """
        Test to see if the contact object is saved into the contact list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list), 1)

    def tearDown(self):
        """
        clean up test case after every run
        """
        Credentials.credential_list = []

    def test_save_multiple_credentials(self):
        """
        test to check if we can save multiple contact
        """
        self.new_credential.save_credential()
        test_credential = Credentials("Instagram", "Temi", "1")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list), 2)

    def test_delete_credential(self):
        """
        test to see if we can remove a credential
        """
        self.new_credential.save_credential()
        test_credential = Credentials("Instagram", "Temi", "1")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_find_credential_by_username(self):
        """
        Test to check if we can find a credential by username
        """
        self.new_credential.save_credential()
        test_credential = Credentials("Instagram", "Temi", "1")
        test_credential.save_credential()

        found_credential = Credentials.find_by_account("Instagram")
        self.assertEqual(found_credential.account_password,
                         test_credential.account_password)

    def test_credential_exists(self):
        """
        Test to check if a contact exists by returning a Boolean
        """

        self.new_credential.save_credential()
        test_credential = Credentials("Instagram", "Temi", "1")
        test_credential.save_credential()

        credential_exists = Credentials.credential_exists("Instagram")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        """
        method that returns a list of all credentials saved
        """
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credential_list)


if __name__ == '__main__':
    unittest.main()
