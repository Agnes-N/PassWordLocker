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

    password = "".join(random.choice(chars) for x in range (size))
    return password

def displayCredential():
    '''
    will return the save credentials
    '''
    return CredentialData.display_credentials()

def deleteCredentials(credential):
    '''
    delete a credential
    '''
    credential.deleteCredential()

def main():
    print("\n")
    print("Welcome to Password Locker")
    print("This App will store your credentails and generate a password for you")

    while True:
        # print("Use these short codes : cc - create a new account, dc - display contacts, fc -find a contact, ex -exit the contact list, del -delete, ce -copy email")

        # short_code = input().lower()
        print("Use these short codes: cac -create new account and si -signin if you are have an account.")
        short_code = input().lower()

        # account_login = input()
        if short_code == "cac":
            print("First name:")
            firstname = input()
            print('\n')
            print("Last name:")
            lastname = input()
            print('\n')
            print("Username:")
            username = input()
            print('\n')
            print("email:")
            emails = input()
            print('\n')

            print("Use these short codes: crp -create a password, gpp -generate a password")
            short_code = input()
            while True:
                if short_code == "crp":
                    print("Password:")
                    password = input()
                    break
                elif short_code == "gpp":
                    password = randomPassword()
                    print('\n')
                    break
                else:                    
                    print("Create new password")
                    break

            saveAccounts(newUsers(firstname, lastname, emails, username, password))
            print("Created successfully.")
            print(f" Username: {username}, password: {password}.")
            print('\n')
            break

        