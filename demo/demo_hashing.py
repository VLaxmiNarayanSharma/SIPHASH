from siphash.siphash import SipHash24
import os

class SecureHashTable:
    def __init__(self):
        self.key = os.urandom(16)  # secret key
        self.table = {}

    def sip(self, s: str):
        return SipHash24(self.key).hash(s.encode())

    def put(self, key, value):
        h = self.sip(key)
        self.table[h] = value

    def get(self, key):
        h = self.sip(key)
        return self.table.get(h)

if __name__ == "__main__":
    ht = SecureHashTable()
    ht.put("username", "laxmi")
    ht.put("role", "student")

    print("Stored:", ht.table)
    print("Get:", ht.get("username"))
