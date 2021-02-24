import hashlib

username1, password1="admin",b"nx12345Usa"
username2, password2="billy", b"nx12345Mexico"
username3, password3="lilly", b"nx12345Aust"

#Hash your password
#MD-5 hash
md5 = hashlib.md5()
md5.update(password1) #or use bytes(password1,'utf-8')
digest=md5.digest()
print("MD5 bytes=",digest) #bytes
print("MD5: {0}".format(md5.hexdigest()))


#SHA-3 hash
HF=hashlib.sha224()
HF.update(password1)
digest=HF.digest()
print("SHA224 bytes=",digest) #bytes
print("SHA224:",digest.hex()) #in hexadevimal rep

'''
#Drawbacks
i. Easy to find hashes of common passwords in the Internet; they can be
used for attacks. 
ii. SHA-1, SHA-2, SHA-3, are easy to compute; they are used for data/file integrity tests;
they are not designed for multi-user passwords storage.
'''

#Salted hash
import hashlib, uuid
salt = uuid.uuid4().bytes #or .hex
HF=hashlib.sha224()
HF.update(password1)
HF.update(salt) #or HF.update(bytes(salt,'utf-8'))
salteddigest = HF.digest()
print("byte salt, digest-SHA224 \n",salt,",", salteddigest)
print("hex salt, digest-SHA224 \n",salt.hex(),",", salteddigest.hex())

'''
#Merits of Salts
i. It is almost impossible to find hash directly on the internet if it is salted. 
However, the salt must be long enough and random.

ii. Rainbow tables do not work with salted hash.

iii. Two users with same password will not have same passwords when stored.

iv. Use at least 16 byte salt.
'''


#Salt + Peppers
#Pepper is just anohter 'salt' but it is specific to an application, is stored differently
import os
pepper=os.urandom(16)#generate 3 bytes of random number.
HF.update(pepper)
saltpepperdigest=HF.digest()
print("byte salt+paper, digest-SHA224 \n",salt,",",pepper,",",saltpepperdigest)
print("byte salt+paper, digest-SHA224 \n",salt.hex(),",",pepper.hex(),",",saltpepperdigest.hex())



#Salt + Pepper + Run(Iteration)
N=pow(2,10)
for i in range(0,N):
    saltpepperdigest=hashlib.sha224(saltpepperdigest).digest()

print("\n\n")
print("byte salt,pepper,N,digest-SHA224")
print(salt,",",pepper,",",N,",",saltpepperdigest)


#Alternatively, using bycrypt library, salt is saved into hash
#pip install py-bcrypt
import bcrypt
hashpasswd=bcrypt.hashpw("mypassword", bcrypt.gensalt(12)) #here 12 is slowness value, it wards of brute force attack
print("hashpasswd:",hashpasswd) #format ($algorithm$number of iterations in power of 2.salt.password-hash
assert bcrypt.checkpw("mypassword",hashpasswd)

print("Other")
#Other functions are:Argon2, scrypt, PBKDF2 (out dated), bcrypt

from passlib.hash import argon2

# generate new salt, hash password
h = argon2.hash("password")
# the same, but with an explicit number of rounds
h=argon2.using(rounds=4).hash("password")
print("hash by argon2",h)
# verify password
assert True==argon2.verify("password", h)
assert False== argon2.verify("wrong", h)

#more:https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html
#more:https://nakedsecurity.sophos.com/2013/11/20/serious-security-how-to-store-your-users-passwords-safely/
#more:https://www.vaadata.com/blog/how-to-securely-store-passwords-in-database/


#Test
'''
os.urandom
hashed_password = hashlib.sha512("mypassword".encode('utf-8') + uuid.uuid4().hex.encode('utf-8')).hexdigest()
print("hashed_password",hashed_password)
'''
