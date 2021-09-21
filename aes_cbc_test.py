# 한국기술교육대학교 컴퓨터공학부 정보보호개론
# 2021년도 1학기
# tested using python3.7 and pycryptodome
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Padding

key = Random.get_random_bytes(16) 
iv = Random.get_random_bytes(16)

print('key='+bytes(key).hex())
print('iv='+bytes(iv).hex())

cipher = AES.new(key, AES.MODE_CBC, iv)

ptext = 'Kim Sangjin is Handsome'
print('plaintext='+ptext);
pad_ptext = Padding.pad(ptext.encode(), AES.block_size)
print('padded plaintext='+bytes(pad_ptext).hex())

ctext = cipher.encrypt(pad_ptext)
print('ciphertext='+bytes(ctext).hex());
print(bytes(ctext).hex())

cipher = AES.new(key, AES.MODE_CBC, iv)
pad_text = cipher.decrypt(ctext)
ptext = Padding.unpad(pad_text, AES.block_size)
print('plaintext='+ptext.decode())