#Hash of a file.
import sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha3 = hashlib.sha3_224()
filename="requirements.txt"
with open(filename, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)
        sha3.update(data)

print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))
print("SHA3-256: {0}".format(sha1.hexdigest()))


import hashlib
BLOCKSIZE = 65536
hasher = hashlib.sha1()
with open('anotherfile.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())