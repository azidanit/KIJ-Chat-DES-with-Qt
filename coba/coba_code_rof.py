import sys

# setting path
sys.path.append('..')

from RSA import RSA
import random

rsa_cls = RSA()
rsa_cls.setAcrossPublicKey(rsa_cls.public_key)
print(rsa_cls.public_key)
print(rsa_cls.private_key)

print("------------------------")
msg = 12
print(msg)
print("------------------------")

e = rsa_cls.encryptOneByte(msg)
print(e)

d = rsa_cls.decrypytOneByte(e)

print(d)
print("------------------------")
en1 = rsa_cls.encryptMsg("JULI SAYANGKUUU")
print(en1)
dc1 = rsa_cls.decryptMsg(en1)
print(dc1)
