import unittest


class MyTest(unittest.TestCase):

    def test_string_multiply(self):
        self.assertEqual("=====", "=" * 5)
