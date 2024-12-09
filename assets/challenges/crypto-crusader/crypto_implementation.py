import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

class CustomRNG:
    def __init__(self, seed=None):
        # Vulnerability: Using time as seed if none provided
        self.seed = seed if seed is not None else int(time.time())
        self.state = self.seed
    
    def next_bytes(self, n):
        # Vulnerability: Weak random number generation
        result = bytearray()
        for _ in range(n):
            self.state = (1103515245 * self.state + 12345) & 0x7fffffff
            result.append(self.state & 0xFF)
        return bytes(result)

class QuantumResistantCipher:
    def __init__(self):
        self.rng = CustomRNG()
        # Vulnerability: Key generated with weak RNG
        self.key = self.rng.next_bytes(32)
        self.iv = self.rng.next_bytes(16)
    
    def encrypt(self, message):
        # Vulnerability: Using CBC mode with PKCS7 padding
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(message) + padder.finalize()
        
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
        encryptor = cipher.encryptor()
        
        return self.iv + encryptor.update(padded_data) + encryptor.finalize()
    
    def decrypt(self, ciphertext):
        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]
        
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        
        # Vulnerability: Padding oracle through timing
        try:
            padded_data = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            time.sleep(0.1)  # Timing leak
            return unpadder.update(padded_data) + unpadder.finalize()
        except padding.InvalidPadding:
            time.sleep(0.2)  # Timing leak
            raise

# Example usage
if __name__ == "__main__":
    cipher = QuantumResistantCipher()
    message = b"quantum_security_breach_detected"
    encrypted = cipher.encrypt(message)
    with open("encrypted_message.bin", "wb") as f:
        f.write(encrypted)
