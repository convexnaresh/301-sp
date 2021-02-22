from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()

print("p=",keyPair.p)
print("q=",keyPair.q)
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
print("\n")



print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))


#Next, encrypt the message using RSA-OAEP encryption scheme (RSA with PKCS#1 OAEP padding) with the RSA public key:
msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)

if msg==decrypted:
    print("Decruption successful, original message retrieved")
else:
    print("Decryption failed")

#http://www.linux-admins.net/2010/09/public-key-cryptography-with-dsa.html
#https://cryptobook.nakov.com/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples