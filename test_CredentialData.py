import unittest

from CredentialData import CredentialData


class TestCredential(unittest.TestCase):
    def setUp(self):
        """
        setUp method
        """
        self.new_credential = CredentialData("twitter", "aggy", "54321")

    def test_init(self):
        """
        testing initialization
        """
        self.assertEqual(self.new_credential.platform, "twitter")
        self.assertEqual(self.new_credential.username, "aggy")
        self.assertEqual(self.new_credential.password, "54321")

    def tearDown(self):

        CredentialData.credentials = []

    def test_save_credential(self):
        """
        test if credential is saved in the credentials list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(CredentialData.credentials), 1)

    def test_display_credentials(self):
        """
        test display credentials method
        """
        self.assertEqual(CredentialData.display_credentials(),
                        CredentialData.credentials)


if __name__ == '__main__':
    unittest.main()
