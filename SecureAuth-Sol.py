'''
Author: Naresh Adhikari, Sru
This is a skeletal program that students need to implement the declared
and defined functions under @TODO annotation, according to the logic/functional requirements stated in assigment-2.pdf.

Students are not expected to midify main() function.
'''
import hashlib
def secure_hashed_passwd(username, passwd):
    import hashlib, uuid
    import os

    '''
    @TODO: Students are required to implement this function.
    using salt+paper+sha3-512 algorithm
    :param username: string repr of username
    :param hpasswd: sha-3-152 string hash value
    :return: True if given values are stored successfully in outfile var; else returns False
    '''

    #use salt and pepper to hash 'hpasswd' using sha-3-512 algorithm
    # Add salt
    salt = uuid.uuid4().hex #.bytes  # or .hex
    HF = hashlib.sha224()
    HF.update(str.encode(passwd,'utf-8'))
    HF.update(str.encode(salt,"utf-8"))  # or HF.update(bytes(salt,'utf-8'))

    # add pepper
    pepper = os.urandom(16).hex() # generate 2 bytes of random number.
    HF.update(str.encode(pepper,"utf-8"))
    saltpepperdigest = HF.hexdigest()

    return salt,pepper,saltpepperdigest

def secure_hashed_passwdV2(username, passwd):
    import hashlib, uuid
    import os

    '''
    @TODO: Students are required to implement this function.
    using salt+paper+sha3-512 algorithm
    :param username: string repr of username
    :param hpasswd: sha-3-152 string hash value
    :return: True if given values are stored successfully in outfile var; else returns False
    '''

    #use salt and pepper to hash 'hpasswd' using sha-3-512 algorithm
    # Add salt
    bytesalt = uuid.uuid4().bytes

    # add pepper
    bytepepper = os.urandom(16)


    HF = hashlib.sha224()

    HF.update(str.encode(passwd,'utf-8')) # or HF.update(bytes(passwd,'utf-8'))
    HF.update(bytesalt)
    HF.update(bytepepper)

    saltpepperdigest = HF.hexdigest()

    return bytesalt.hex(),bytepepper.hex(),saltpepperdigest


def salt_pepper_digest(salt,pepper,inputstr):
    import hashlib

    HF = hashlib.sha224()
    HF.update(str.encode(inputstr,'utf-8'))
    HF.update(str.encode(salt,'utf-8'))

    #add pepper
    HF.update(str.encode(pepper,'utf-8'))  # generate 3 bytes of random number.
    saltpepperdigest = HF.hexdigest()
    return saltpepperdigest

def salt_pepper_digestV2(hexsalt,hexpepper,inputstr):
    import hashlib

    HF = hashlib.sha224()
    bytesalt=bytes.fromhex(hexsalt)
    bytepepper = bytes.fromhex(hexpepper)

    #add pepper
    HF.update(str.encode(inputstr,'utf-8'))
    HF.update(bytesalt)
    HF.update(bytepepper)

    saltpepperdigest = HF.hexdigest()
    return saltpepperdigest

def verify_hashed_passwd(username, passwd):
    '''
    @TODO: Students are required to implement this function.

    Server side verifies login credentials username and password
    :param username:
    :param hpasswd:
    :return:
    '''
    #databse file with username and hashed-password.
    infile="hlogins.dat"
    #open the file to read
    fd=open(infile,"r")
    #read the infile line by line to retrive a matching row with first
    user_pswdrows=fd.readlines()
    for row in user_pswdrows:
        data=row.split(",")
        uname=data[0]
        salt=data[1]
        pepper=data[2]
        stored_hpasswd=data[3] #stored digest

        if username == uname:
            #obt_passwd=salt_pepper_digest(salt,pepper,passwd)
            obt_passwd=salt_pepper_digestV2(salt,pepper,passwd)
            if stored_hpasswd == obt_passwd:
                return True

    #username,password not matched!
    return False

def main():
    '''Do not modify this function.'''

    import hashlib, uuid
    import os

    lusername=["shyamal@gmail.com",
                "brutforce@yahoo.com",
                "lifegivesalot@protonmail.com",
                "rainbow@sru.edu",
                "ghana@makai.com",
                "david@inst.edu",
                "buttlerbusiness@sru.edu",
                "myChurch45@state.edu"]
    lpasswd=["pass$1290Red",
            "fail$567Blue",
            "rainB0w159$",
            "lglot$$$Tatoo",
            "ghana456$$909",
            "DavI0234$09",
            "IsBulltop345",
            "xCrosTop24"]

    # open file outfile in write mode.
    outfile="hlogins.dat"
    fd = open(outfile, "w+")
    #@server: call method for each usernames, passwords.
    for i in range(0,len(lusername)):
        username=lusername[i]
        passwd=lpasswd[i]
        salt,pepper,saltpepperdigest=secure_hashed_passwdV2(username,passwd)
        if i in [3,7,1]:continue
        fd.write(username + "," + str(salt) + "," + str(pepper) + "," + saltpepperdigest+","+"$\n")
    fd.close()

    for j in range(0,len(lusername)):
        uname=lusername[j]
        passwd=lpasswd[j]
        result=verify_hashed_passwd(uname,passwd)
        if not result:
            print("<!> Login failed for user ",uname)
        else:
            print("Login succesful for user ",uname)

if __name__ == "__main__":
    main()