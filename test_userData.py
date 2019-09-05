import unittest
from userData import UserData

class TestuserData(unittest.TestCase):
    def setUp(self):
        '''
        set up method
        '''
        self.newUser = UserData("Aggy","Reina","aggyreina@gmail.com","aggy","12345")
    
    def test_init(self):
        '''
        test initialization of the class
        '''
        self.assertEqual(self.newUser.firstName, "Aggy")
        self.assertEqual(self.newUser.lastName, "Reina")
        self.assertEqual(self.newUser.email, "aggyreina@gmail.com")
        self.assertEqual(self.newUser.userName, "aggy")
        self.assertEqual(self.newUser.password, "12345")

    def tearDown(self):
        '''
        Function to clean up the existing inputs
        '''
        UserData.createAccount = []

    def test_save(self):
        '''
        A function that will help us to save the created account
        '''
        self.newUser.saveAccount()
        self.assertEqual(len(UserData.createAccount),1)

# if _name_ == '_main_':
#     unittest.main()

