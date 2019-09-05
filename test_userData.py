import unittest
from userData import UserData
import pyperclip


class TestuserData(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method
        '''
        self.newUser = UserData(
            "Aggy", "Reina", "aggyreina@gmail.com", "aggy", "12345")

    def test_init(self):
        '''
        test initialization of the class
        '''
        self.assertEqual(self.newUser.firstName, "Aggy")
        self.assertEqual(self.newUser.lastName, "Reina")
        self.assertEqual(self.newUser.email, "aggyreina@gmail.com")
        self.assertEqual(self.newUser.userName, "aggy")
        self.assertEqual(self.newUser.password, "12345")

    def test_save(self):
        '''
        test_save test case to test if the created account is saved into the account list
        '''
        self.newUser.saveAccount()
        self.assertEqual(len(UserData.createAccount), 1)

    def tearDown(self):
        '''
        Function to clean up after each test case has run
        '''
        UserData.createAccount = []

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple usernames to our user_names
        """
        self.newUser.saveAccount()
        test_userData = UserData(
            "Aggy", "Reina", "aggyreina@gmail.com", "aggy", "12345")
        test_userData.saveAccount()
        self.assertEqual(len(UserData.createAccount), 2)


if __name__ == '__main__':
    unittest.main()
