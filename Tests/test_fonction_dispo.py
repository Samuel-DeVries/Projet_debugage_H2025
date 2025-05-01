import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Code")))
from fonction_dispo import dispo
class Test_fonction_dispo(unittest.TestCase):
    def test_dispo_1(self):
        self.assertEqual(type(dispo("2025-04-30", "B1")), dict)
if __name__ == "__main__":
    unittest.main()
