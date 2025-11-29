import pytest
from siphash.siphash import SipHash24
from siphash.test_vectors import TEST_KEY, TEST_VECTORS

def test_siphash_vectors():
    for msg, expected in TEST_VECTORS:
        h = SipHash24(TEST_KEY).hash(msg.encode())
        assert h == expected, f"Fail: {msg}"
