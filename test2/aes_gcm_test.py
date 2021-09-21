# 한국기술교육대학교 컴퓨터공학부 정보보호개론
# 2021년도 1학기
# tested using python3.7 and pycryptodome
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Padding

key = Random.get_random_bytes(16) 
nonce = Random.get_random_bytes(12)

print('key='+bytes(key).hex())
print('nonce='+bytes(nonce).hex())

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

ptext = 'Kim Sangjin is Handsome'
print('plaintext='+ptext);
aad = 'associated data'
cipher.update(aad.encode())

ctext, tag = cipher.encrypt_and_digest(ptext.encode())
print('ciphertext='+bytes(ctext).hex());
print('tag='+bytes(tag).hex());

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
cipher.update(aad.encode())
ptext = cipher.decrypt_and_verify(ctext, tag)
print('plaintext='+ptext.decode())