class UserData:
    '''
    A class that will used to create a new account
    '''
    createAccount = []

    def __init__(self, firstName, lastName, email, userName, password):
        '''
        Initialization of the class
        '''
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userName = userName
        self.password = password

    def saveAccount(self):
        '''
        A function to save new user to createAcount list
        '''
        UserData.createAccount.append(self)

    @classmethod
    def userLogin(cls, generatedName, generatedPassword):
        '''
        function to check if the user exist
        '''
        for user in UserData.createAccount:
            if user.userName == generatedName and generatedPassword == generatedPassword:
                return user
            return False
