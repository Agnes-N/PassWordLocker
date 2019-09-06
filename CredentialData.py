class CredentialData:

    """
    create new instances
    """

    credentials = []

    def __init__(self, platform, username, password):

        self.platform = platform
        self.username = username
        self.password = password

    def saveCredentials(self):
        """
        save credential objects to the credential list
        """
        CredentialData.credentials.append(self)

    @classmethod
    def displayCredentials(cls):
        """
        displays the credentials 
        """
        return cls.credentials
