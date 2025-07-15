#!/usr/bin/env python3
"""
Run all tests for the Apollog package.
"""

import unittest
import os
import sys

def run_tests():
    """Run all tests in the tests directory."""
    # Get the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set up the test suite
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.join(script_dir, 'tests'))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return 0 if all tests passed, 1 otherwise
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests())
