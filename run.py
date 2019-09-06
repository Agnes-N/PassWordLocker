#!/usr/bin/env python3.6
import random
import string

from userData import UserData
from CredentialData import CredentialData

def newUsers(name1, name2, emailAddress, username, passWord):
    '''
    creating new user
    '''
    newUser = UserData(name1, name2, emailAddress, username, passWord)
    return newUser

def saveAccounts(account):
    '''
    save new account
    '''
    account.saveAccount()

def checkUser(generatedName, generatedPassword):
    '''
    function to check if user exist
    '''
    userExist = UserData.userLogin(generatedName, generatedPassword)
    return userExist

def addCredential(account, accountName, accountPassword):
    '''
    function to add credential
    '''
    addedCredential = CredentialData(account, accountName, accountPassword)
    return addedCredential

def saveCredentials(credential):
    '''
    save credential
    '''
    credential.saveCredentials()

def randomPassword():
    '''
    function to generate random password
    '''
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    
    return password