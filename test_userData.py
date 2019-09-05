import unittest
from userData import UserData

class TestuserData(unittest.TestCase):
    def setUp(self):
        '''
        set up method
        '''
        self.newUser = UserData("Aggy","Reina","aggyreina@gmail.com","aggy","12345")
    
    # def test_init(sel):
    #     '''
    #     test initialization of the class
    #     '''
    #     sel.assertEqual(self.newUser.firstName, "Aggy")
