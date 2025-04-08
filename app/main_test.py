from main import return_backwards_string,get_mode
import unittest
import os

class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        test_string = "hello"
        expected_result = "olleh"
        self.assertEqual(return_backwards_string(test_string), expected_result)

    def test_get_mode(self):
        self.assertEqual(os.environ.get("MODE"), get_mode())

if __name__ == '__main__':
    unittest.main()