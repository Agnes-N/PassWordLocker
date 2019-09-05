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

    # @classmethod