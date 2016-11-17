import unittest
import sys

"""
Run:

    > python unittest_example.py

    > python -m unittest -v unittest_example


    -v to more info (verbose)

    python unittest_example.py -v MyTest to execute only a class in the test file.
    python unittest_example.py -v TestStringMethods.test_upper


"""


def stupid_function(x):
    return x + 1

class stupid_test(unittest.TestCase):
    def test(self):
        self.assertEqual(stupid_function(3), 4)

if __name__ == '__main__':
    unittest.main()
