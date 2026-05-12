# test_nodesync.py
"""
Tests for NodeSync module.
"""

import unittest
from nodesync import NodeSync

class TestNodeSync(unittest.TestCase):
    """Test cases for NodeSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeSync()
        self.assertIsInstance(instance, NodeSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
