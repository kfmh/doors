import unittest
from src.doors.ciphers.caesar_cipher import Caeser_Cipher


class Test_caesar_cipher(unittest.TestCase):
    def setUp(self):
        self.cipher = Caeser_Cipher()
        
    def test_encryption_returns_string(self):
        result = self.cipher.encryption('abc', 3)
        self.assertIsInstance(result, str, 'Returns string')
    
    def test_encryption(self):
        self.assertEqual(self.cipher.encryption('abc', 3), 'def')

    def test_decryption_return_string(self):
        result = self.cipher.decryption('abc', 3)
        self.assertIsInstance(result, str, 'Returns string')

    def test_decryption(self):
        self.assertEqual(self.cipher.decryption('def', 3), 'abc')


if __name__ == '__main__':
    unittest.main()
