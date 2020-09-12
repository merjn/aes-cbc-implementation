def xor(first, second) -> bytes:
    return bytes([b1 ^ b2 for b1, b2 in zip(first, second)])