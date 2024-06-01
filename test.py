import unittest
from wc import *

test_file = "test.txt"


class TestWCTool(unittest.TestCase):
	test_file = "test.txt"

	## basic test functions

	def test_word(self):
		self.assertEqual(count_words(test_file), 19)

	def test_line(self):
		self.assertEqual(count_lines(test_file), 7)

	def test_byte(self):
		self.assertEqual(count_bytes(test_file), 102)

	def test_char(self):
		self.assertEqual(count_char(test_file), 102)


if __name__ == '__main__':
	unittest.main()