# 한국기술교육대학교 컴퓨터공학부 정보보호개론
# 2021년도 1학기
# tested using python3.7 and pycryptodome
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Padding
from Crypto.Util import Counter

key = Random.get_random_bytes(16) 
iv = Random.get_random_bytes(16)

print('key='+bytes(key).hex())
print('iv='+bytes(iv).hex())

ctr = Counter.new(128, initial_value=int.from_bytes(iv, 'big'))
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

ptext = 'Kim Sangjin is Handsome'
print('plaintext='+ptext);

ctext = cipher.encrypt(ptext.encode())
print('ciphertext='+bytes(ctext).hex());
print(bytes(ctext).hex())

cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
ptext = cipher.decrypt(ctext)
print('plaintext='+ptext.decode())