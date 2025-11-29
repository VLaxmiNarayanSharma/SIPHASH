A clean, educational, research-oriented implementation of SipHash-2-4, the fast, cryptographically secure keyed hash function introduced in:

“SipHash: a fast short-input PRF” — ACM CCS 2012 (A Conference)*
Jean-Philippe Aumasson & Daniel J. Bernstein

This project implements SipHash-2-4 in Python, provides a small hash table demo, and includes unit tests to validate correctness.
It is designed for M.Tech / Research Projects, CNS Lab, and academic demonstrations of message-authentication hashes.


📌 Features
✔️ Pure Python implementation of SipHash-2-4

Fully matches the algorithm from the research paper

Uses SipHash compression and finalization rounds (2–4 configuration)

✔️ Simple demo program

Demonstrates how SipHash resists hash-flooding attacks

Uses SipHash to build a secure dictionary-style HashTable

✔️ Unit tests

Ensures correctness of:

Round operations

Hash outputs

Padding

Compression

🔧 Installation

Clone the repository:

git clone https://github.com/yourusername/siphash.git
cd siphash


(Optional) Create a virtual environment:

python -m venv venv
venv\Scripts\activate    # Windows


Install requirements (if any):

pip install -r requirements.txt

▶️ How to Run
1️⃣ Run Unit Tests
python -m tests.test_siphash

2️⃣ Run Demo (HashTable using SipHash)
python -m demo.demo_hashing


Expected output:

Stored: {1088776009278692853: 'student'}
Get: student
