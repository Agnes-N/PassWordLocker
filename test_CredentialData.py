import unittest

from CredentialData import CredentialData


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        setUp method
        """
        self.new_credential = CredentialData("instagram", "reina", "12345") 

    def test_init(self):
        """
        testing initialization
        """
        self.assertEqual(self.new_credential.platform, "instagram")
        self.assertEqual(self.new_credential.username, "reina")
        self.assertEqual(self.new_credential.password, "12345")
    
    def save_credential(self):

        """
        save credential objects to the credential list
        """
        CredentialData.credentials.append(self)