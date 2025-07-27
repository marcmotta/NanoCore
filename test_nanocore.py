# test_nanocore.py
"""
Tests for NanoCore module.
"""

import unittest
from nanocore import NanoCore

class TestNanoCore(unittest.TestCase):
    """Test cases for NanoCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NanoCore()
        self.assertIsInstance(instance, NanoCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NanoCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
