'''
Date: 021/15/2021
Authors: Naresh Adhikari, Lucas Luczak, Marck ..

SLCM is a login credential management module.
'''

from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
from Crypto.Cipher import AES
import re

def getusername_paswd():
    '''
    Author: Naresh Adhikari
    Inputs:
    Outputs: Returns valid username and password entered by a user
    '''
    #function logic
    username=input("Enter your username: <Enter your email address>")


    #validate username variable
    regex = r'^[a-z0-9]+[\._]*[a-z0-9]*[@]\w+[.]\w{2,3}$'

    uvalid=False
    if re.search(regex,username):
        uvalid=True

    while uvalid==False:
        username = input("Enter your username: <Enter your email address>")
        if re.search(regex, username):
            uvalid = True
        else:
            uvalid=False

    #validate password variable
    password=input("Password rules are:"
                   "\n 1. at least 8 characters, "
                   "\n 2. has at least one alphabet,"
                   "\n 3. has at least one digit, "
                   "\n 4. has at a character in {#,$,%,*}"
                   "\n Enter your password:")
    regex2 = r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)'
    pvalid = False
    if re.search(regex2,password):
        pvalid=True
    while pvalid==False:
        password = input("Enter your password, must have 8 characters,"
                         "with at least one alphabet, one digit"
                         "and a character from [#,$,%,*]\n"
                         "\n 1. at least 8 characters, "
                         "\n 2. has at least one alphabet,"
                         "\n 3. has at least one digit, "
                         "\n 4. has at a character in {#,$,%,*}"
                         "\n Enter your password:")
        if re.search(regex2,password):
            pvalid=True
        else:
            pvalid=False
    if uvalid and pvalid:
        return username, password

def secure_store(username, password):
   '''
   Author:
   Inputs:
   Outputs:
    :return:
    '''
   outputfile="credential.dat"
   fd = open(outputfile,'ra')

   outputfile = "credential.dat"
   fd = open(outputfile, 'w+')

   # encrypt password with AES algorithm

   password = bytes(password, 'utf-8')
   key = get_random_bytes(16)
   cipher = AES.new(key, AES.MODE_CBC)
   ct_bytes = cipher.encrypt(pad(password, AES.block_size))

   iv = b64encode(cipher.iv).decode('utf-8')
   ct = b64encode(ct_bytes).decode('utf-8')

   #store iv and ciphertext
   fd.write(username + ","+str(iv)+"," + ct)

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