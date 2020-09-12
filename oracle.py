from Crypto.Cipher import AES

from cbc import CBC
from keygen import pseudorandom
import random


def encrypt_oracle(p: bytes):
    c = b""
    amount = random.randrange(5, 10)
    c += pseudorandom(amount)

    strategy = random.randrange(0, 2)
    print(strategy)
    if strategy == 0:
        aes = AES.new(pseudorandom(16), AES.MODE_ECB)
        c += bytes(aes.encrypt(p))
    else:
        iv = pseudorandom(16)
        aes = CBC(pseudorandom(16), iv)
        c += aes.encrypt(str(p))

    amount = random.randrange(5, 10)
    c += pseudorandom(amount)

    return c
