from cbc import CBC
import base64

from keygen import pseudorandom
from oracle import encrypt_oracle
from xor import xor

with open('10.txt') as f:
    k = b'YELLOW SUBMARINE'
    iv = b"\x00\x00\x00\x00" * 4
    decoded = base64.b64decode(f.read())
    aes = CBC(k, iv)
    p = aes.decrypt(decoded)
    print(encrypt_oracle(b"aaaaaaaaaaaaaaaa"))
