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
    '''save new account
    '''
    account.saveAccount()

