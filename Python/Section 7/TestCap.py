# First test simple things, then the more complex things

import unittest
import Cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = Cap.cap_text(text)
        self.assertEqual(result, "Python")

    def test_mult_words(self):
        text = "great python"
        result = Cap.cap_text(text)
        self.assertEqual(result, "Great Python")

if __name__ == "__main__":
        unittest.main()