# siphash.py — SipHash-2-4 implementation

def rotate_left(x, b):
    return ((x << b) & 0xffffffffffffffff) | (x >> (64 - b))

class SipHash24:
    def __init__(self, key: bytes):
        assert len(key) == 16, "Key must be 128-bit"
        k0 = int.from_bytes(key[:8], 'little')
        k1 = int.from_bytes(key[8:], 'little')

        self.v0 = 0x736f6d6570736575 ^ k0
        self.v1 = 0x646f72616e646f6d ^ k1
        self.v2 = 0x6c7967656e657261 ^ k0
        self.v3 = 0x7465646279746573 ^ k1

    def compress(self):
        v0, v1, v2, v3 = self.v0, self.v1, self.v2, self.v3

        v0 = (v0 + v1) & 0xffffffffffffffff
        v1 = rotate_left(v1, 13)
        v1 ^= v0
        v0 = rotate_left(v0, 32)

        v2 = (v2 + v3) & 0xffffffffffffffff
        v3 = rotate_left(v3, 16)
        v3 ^= v2

        v0 = (v0 + v3) & 0xffffffffffffffff
        v3 = rotate_left(v3, 21)
        v3 ^= v0

        v2 = (v2 + v1) & 0xffffffffffffffff
        v1 = rotate_left(v1, 17)
        v1 ^= v2
        v2 = rotate_left(v2, 32)

        self.v0, self.v1, self.v2, self.v3 = v0, v1, v2, v3

    def hash(self, msg: bytes) -> int:
        v0, v1, v2, v3 = self.v0, self.v1, self.v2, self.v3

        # Process full 8-byte blocks
        i = 0
        while i + 8 <= len(msg):
            m = int.from_bytes(msg[i:i+8], 'little')
            v3 ^= m
            self.compress()
            self.compress()
            v0 ^= m
            i += 8

        # Final block
        # length fits in 1 byte as per SipHash spec
        length_byte = len(msg) & 0xff
        pad = (length_byte << 56).to_bytes(8, 'little')

        last = msg[i:] + pad[len(msg[i:]):]
        m = int.from_bytes(last, 'little')

        v3 ^= m
        self.compress()
        self.compress()
        v0 ^= m

        # Finalization
        v2 ^= 0xff
        for _ in range(4):
            self.compress()

        return (v0 ^ v1 ^ v2 ^ v3) & 0xffffffffffffffff
