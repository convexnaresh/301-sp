'''
Author: Naresh Adhikari, Sru
This is skeletal program that students need to implement the declared
and defined functions according to the logic/functional requirements stated in assigment-2.pdf.

Students are not expected to midify main() function.
'''
import hashlib

def secure_hashed_passwd(username, hpasswd):
    '''
    @TODO: Students are required to implement this function.

    Stores given username and hpasswd in outfile after computing hash value of hpasswd input
    using salt+paper+sha3-512 algorithm
    :param username: string repr of username
    :param hpasswd: sha-3-152 string hash value
    :return: True if given values are stored successfully in outfile var; else returns False
    '''
    outfile="hcredential.dat"

    #use salt and pepper to hash 'hpasswd' using sha-3-512 algorithm


    #open file outfile in write mode.
    #Write data in the file

    #display a message "Credentials stored successfully"

    #close the file

    return True


def verify_hashed_passwd(username, hpasswd):
    '''
    @TODO: Students are required to implement this function.

    :param username:
    :param hpasswd:
    :return:
    '''

    infile="hcredential.dat"

    #open the file to read
    #read the infile line by line to retrive a matching row with first
    # field value equal to username supplied in this funciton.
    # close the file

    #compute tempo_hash using salt,pepper (retrived above) and sha-3-512 algorithm


    #check if tempo_hash and hpasswd matches.
        #Display message if matches
        #return True

        #Display Message if NOT-matches
        #return False

    return True

def main():
    '''Do not modify this function.'''

    import hashlib, uuid
    import os

    lusername=["shyamal@gmail.com","brutforce@yahoo.com","rainbow@sru.edu"]
    lpasswd=["pass$1290Red","fail$567Blue","rainB0w159$"]
    lhpasswd = []

    print("Create account in servers for the following username and hash of user's password.")
    #ClientSide:hash using salt+pepper+sha-3-512
    for idx in range(0, len(lusername)):
        #Add salt
        salt = uuid.uuid4().bytes  # or .hex
        HF = hashlib.sha224()
        HF.update(str.encode(lpasswd[idx]))
        HF.update(salt)  # or HF.update(bytes(salt,'utf-8'))

        #add pepper
        pepper = os.urandom(16)  # generate 3 bytes of random number.
        HF.update(pepper)
        saltpepperdigest = HF.hexdigest()
        lhpasswd+=[saltpepperdigest]
        #print("client-",idx,lusername[idx],salt,pepper,saltpepperdigest)
        print(idx,",",lusername[idx],",",saltpepperdigest)

    #call methods to store all of the values.
    for i in range(0,len(lhpasswd)):
        username=lusername[i]
        hpasswd=lhpasswd[i]
        secure_hashed_passwd(username,hpasswd)
        verify_hashed_passwd(username,hpasswd)

if __name__ == "__main__":
    main()