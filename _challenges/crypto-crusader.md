---
layout: challenge
title: "Crypto Crusader"
difficulty: Hard
category: Cryptography
questions:
  - title: "Key Generation Vulnerability"
    description: "What component of the key generation process contains a critical vulnerability?"
    answer: "random number generator"
  - title: "Encryption Weakness"
    description: "Which encryption mode is vulnerable to the padding oracle attack in this implementation?"
    answer: "cbc"
  - title: "Decrypted Message"
    description: "What is the decrypted message after exploiting the vulnerabilities?"
    answer: "quantum_security_breach_detected"
files:
  - name: "crypto_implementation.py"
    path: "/assets/challenges/crypto-crusader/crypto_implementation.py"
  - name: "encrypted_message.bin"
    path: "/assets/challenges/crypto-crusader/encrypted_message.bin"
  - name: "key_generation.log"
    path: "/assets/challenges/crypto-crusader/key_generation.log"
hints:
  - "Check the seed value used in the random number generator"
  - "Look for timing differences in padding validation"
  - "The key generation logs contain important timestamps"
---

## Background
A new encryption algorithm claims to be quantum-resistant, but security researchers suspect implementation flaws. Your task is to analyze the algorithm and find potential vulnerabilities that could compromise its security.

## Objective
Through analysis of the provided implementation:
1. Find the vulnerability in the key generation process
2. Identify the weak encryption mode
3. Exploit the vulnerabilities to decrypt the message

## Technical Details
The encryption scheme uses:
- Custom random number generator
- Block cipher in CBC mode
- PKCS7 padding
- Post-quantum primitives

## Analysis Areas
1. Key Generation
   - Random number generator implementation
   - Seed generation process
   - Key derivation function

2. Encryption Process
   - Block cipher mode
   - Padding mechanism
   - Error handling

3. Implementation Review
   - Timing analysis
   - Error messages
   - Memory handling

## Notes
- Focus on both algorithmic and implementation weaknesses
- Consider side-channel attacks
- Document your exploitation process

Remember to approach the analysis systematically and document each step of your investigation.
