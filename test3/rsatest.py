# 한국기술교육대학교 컴퓨터공학부 정보보호개론
# 2021년도 1학기
# tested using python3.7 and pycryptodome
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256

rng = Random.new().read
RSAKeyPair = RSA.generate(1024, rng)

print(RSAKeyPair.publickey().exportKey())

cipher_rsa = PKCS1_OAEP.new(RSAKeyPair)
ctext = cipher_rsa.encrypt("Kim Sangjin".encode())

print(bytes(ctext).hex())
ptext = cipher_rsa.decrypt(ctext)

print(ptext.decode())

sigtext = "hello"
w = SHA256.new(sigtext.encode())
sigblock = PKCS1_PSS.new(RSAKeyPair).sign(w)

verifier = PKCS1_PSS.new(RSAKeyPair)
try:
    verifier.verify(w, sigblock)
    print("the signature is authentic")
except (ValueError, TypeError):
    print("the signature is not authentic")