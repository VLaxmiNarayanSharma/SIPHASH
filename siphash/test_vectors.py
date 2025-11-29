TEST_KEY = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

TEST_VECTORS = [
    ("", 0x726fdb47dd0e0e31),
    ("a", 0x2ba3e8e9a71148ca),
    ("abc", 0x5dbcfa53aa2007a5),
    ("message digest", 0xb670bf0a59c7f5c9),
    ("abcdefghijklmnopqrstuvwxyz", 0x87162f9dd999915f),
]
