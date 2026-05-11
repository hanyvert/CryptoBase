# test_cryptobase.py
"""
Tests for CryptoBase module.
"""

import unittest
from cryptobase import CryptoBase

class TestCryptoBase(unittest.TestCase):
    """Test cases for CryptoBase class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoBase()
        self.assertIsInstance(instance, CryptoBase)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoBase()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
