from Crypto.Random import get_random_bytes


def pseudorandom(size: int) -> bytes:
    random = get_random_bytes(size)
    return random


