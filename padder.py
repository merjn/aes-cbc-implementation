class PKCS7Padding:
    block_size = 16

    def pad(self, data) -> bytes:
        length = len(data)
        size = self.block_size - (length % self.block_size)
        if size == 0:
            size = self.block_size

        pad = chr(size)
        result = data + pad * size
        return str.encode(result)

    def unpad(self, data):
        size = int(data[len(data)-1])
        return data[:len(data)-size]
