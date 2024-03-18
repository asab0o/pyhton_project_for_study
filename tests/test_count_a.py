import unittest
from src.count_a import count_a

class TestCountA(unittest.TestCase):
    def test_with_a(self):
        self.assertEqual(count_a("apple"), 1)
        self.assertEqual(count_a("Anna"), 2)
    
    def test_without_a(self):
        print("test_without_a 開始")
        self.assertEqual(count_a("test"), "nothing.")
        print("test_without_a 終了")
    
    def test_empty_string(self):
        self.assertEqual(count_a(""), "nothing.")

if __name__ == "__main__":
    unittest.main()
