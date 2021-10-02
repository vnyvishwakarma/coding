import program
import unittest


class TestCode(unittest.TestCase):
    def test_case(self):
        first = [3, 2, 4, 11, 8, 9, 5, 6, 22, -5, 7]
        second = [11, 6, -5]

        print(self.assertTrue(program.isSubsequence(first, second)))
