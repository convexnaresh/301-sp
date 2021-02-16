'''
Date: 021/15/2021
Authors: Naresh Adhikari, Lucas Luczak, Marck ..

SLCM is a login credential management module.
'''

from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
from Crypto.Cipher import AES

def getusername_paswd():
    '''
    Author: Naresh Adhikari
    Inputs:
    Outputs: Returns valid username and password entered by a user
    '''
    #function logic
    username=input("Enter your username: <Enter your email address>")
    password=input("Password rules are:"
                   "\n 1. at least 8 characters, "
                   "\n 2. has at least one alphabet,"
                   "\n 3. has at least one digit, "
                   "\n 4. has at a character in {#,$,%,*}"
                   "\n Enter your password:")
    validboth=False
    #validate username variable

    #validate password variable

    if validboth:
        return username, password
    else:
        return None,None

def secure_store(username, password):
   '''
   Author:
   Inputs:
   Outputs:
    :return:
    '''
   outputfile="credential.dat"
   fd = open(outputfile,'ra')

   #encrypt password with AES algorithm
   encrypted_password=''
   #store username and encypted password in the file.

   #display message.
   print("username and password saved in ", outputfile)

def main():
    vusername,vpassword=getusername_paswd() #get valid username and password
    if vusername and vpassword:
        secure_store(vusername, vpassword)
    else:
        print("username and password saved failed.")

#invoke main()
main()