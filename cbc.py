from padder import PKCS7Padding
from xor import xor
from Crypto.Cipher import AES


class CBC:
    iv: bytes
    block_size = 16
    _ecb: AES
    _padder: PKCS7Padding

    def __init__(self, k: bytes, iv: bytes):
        self.iv = iv
        self._ecb = AES.new(k, AES.MODE_ECB)
        self._padder = PKCS7Padding()
        self._padder.block_size = self.block_size

    def encrypt(self, p):
        p = self._padder.pad(p)
        c = b""
        for i in range(0, len(p), self.block_size):
            current_block = p[i:i+self.block_size]
            if i == 0:
                temp = xor(current_block, self.iv)
                c += self._ecb.encrypt(temp)
            else:
                previous_block = p[i-self.block_size:i]
                temp = xor(current_block, previous_block)
                c += self._ecb.encrypt(temp)

        return c

    def decrypt(self, c):
        """
        Reverse the encrypt operation.
        The encrypt operation first xors the current and previous block, and then performs
        the encryption. In order to decrypt this data, we need to reverse that procedure;
        first, decrypt a block of c, then xor it. This will result in p.
        :param c:
        :return:
        """
        p = b""
        for i in range(0, len(c), self.block_size):
            current_block = c[i:i + self.block_size]
            if i == 0:
                temp = self._ecb.decrypt(current_block)
                p += xor(temp, self.iv)
            else:
                previous_block = c[i-self.block_size:i]
                temp = self._ecb.decrypt(current_block)
                p += xor(temp, previous_block)

        p = self._padder.unpad(p)
        return p
